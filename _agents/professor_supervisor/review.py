#!/usr/bin/env python3
"""
Professor Supervisor — Quality Gate Reviewer
Reviews every course file against the 10 quality gates.
Output: APPROVED / REVISE / REJECT with rubric breakdown.
"""
import os
import re
import sys
import json
import argparse
from pathlib import Path


# Quality gate definitions
TEMPLATE_MARKERS = [
    r'\[TBD\]', r'待補充', r'placeholder', r'Lorem ipsum',
    r'CORE_DEEPDIVE_ONE', r'CORE_DEEPDIVE_TWO', r'CORE_DEEPDIVE_THREE',
    r'T0 — Core', r'T1 — Methods', r'T2 — Applications',
    r'PLACEHOLDER', r'\[TODO\]', r'Fixme', r'fixme',
    r'^\s*XXX\b', r'\$\{.*\}',  # unfilled templates
]

SCHOLAR_HINT = re.compile(
    r'\b('
    r'Newton|Euler|Lagrange|Hamilton|Maxwell|Boltzmann|Fourier|'
    r'Betti|Cauchy|Poisson|Navier|Stokes|Reynolds|Prandtl|von Kármán|'
    r'Bohr|Heisenberg|Schrödinger|Dirac|Fermi|Bose|Einstein|Planck|'
    r'Hemond|Sigmond|Sigmund|Bendsøe|Holzapfel|Ogden|Simo|Taylor|'
    r'Mises|Tresca|Mohr|Coulomb|von Mises|Goodman|Miner|Paris|'
    r'Rankine|Terzaghi|Casagrande|Darcy|Bernoulli|Reynolds|Froude|'
    r'Manning|Chezy|Dupuit|Theis|Jacob|Boussinesq|'
    r'Boltzmann|Gibbs|Arrhenius|Eyring|Polanyi|Marcus|'
    r'Bourouiba|Wells|Duguid|Chao|Baron|Fennelly|Marr|'
    r'Stumm|Schwarzenbach|Girard|Sposito|Bradl|'
    r'Bowles|AISC|ACI|Eurocode|British Standard|BS|'
    r'Braudel|Hobsbawm|Thompson|Anderson|Tilly|Mayer|Hobsbawm|'
    r'von Ranke|Bloch|Marc Bloch|Febvre|'
    r'Farin|Beier|Hoppe|Botsch|Kobbelt|Alliez|'
    r'Papadimitriou|Tsitsiklis|Bertsekas|Nesterov|Boyd|Vandenberghe|'
    r'Girard|Au|Christensen|Waas|Anand|Hart|'
    r'Gao|Baer|Nadler|Wagner|Hill|Hutchinson|Rice'
    r')\b'
)

YEAR_HINT = re.compile(r'\b(1[6-9]\d{2}|20\d{2})\b')


def gate1_length(content: str) -> int:
    """File must be >= 400 lines."""
    lines = content.count('\n')
    if lines >= 400:
        return 10
    if lines >= 300:
        return 5
    if lines >= 200:
        return 2
    return 0


def gate2_format(content: str) -> int:
    """袁騰飛 sections present."""
    score = 0
    if re.search(r'問題 1|心智模型|mental model|5.*core', content, re.IGNORECASE):
        score += 3
    if re.search(r'問題 2|根本分歧|disagree|divergence', content, re.IGNORECASE):
        score += 3
    if re.search(r'問題 3|深度問題|10.*question', content, re.IGNORECASE):
        score += 3
    if re.search(r'深入|deep dive|Deep Dive', content, re.IGNORECASE):
        score += 3
    if re.search(r'解答|solution|Solution', content, re.IGNORECASE):
        score += 3
    return min(score, 15)


def gate3_citations(content: str) -> int:
    """Real scholars with year."""
    scholars = set(SCHOLAR_HINT.findall(content))
    years = YEAR_HINT.findall(content)
    # Score: scholars * 1 + (years with scholar) * 1
    if len(scholars) >= 8 and len(years) >= 5:
        return 15
    if len(scholars) >= 5 and len(years) >= 3:
        return 12
    if len(scholars) >= 3:
        return 8
    if len(scholars) >= 1:
        return 4
    return 0


def gate4_specificity(content: str) -> int:
    """Numbers + equations."""
    equations = re.findall(r'\$\$.*\$\$|\$[^$\n]+\$', content)
    numbers = re.findall(r'\b\d+\.?\d*\b', content)
    if len(equations) >= 8 and len(numbers) >= 30:
        return 15
    if len(equations) >= 5 and len(numbers) >= 15:
        return 12
    if len(equations) >= 3 and len(numbers) >= 10:
        return 8
    if len(equations) >= 1:
        return 4
    return 0


def gate5_bilingual(content: str) -> int:
    """中英對照."""
    cn = re.findall(r'[\u4e00-\u9fff]', content)
    if len(cn) >= 500:
        return 10
    if len(cn) >= 200:
        return 7
    if len(cn) >= 100:
        return 4
    return 0


def gate6_no_placeholder(content: str) -> int:
    """No [TBD] / 待補充 / Lorem."""
    hits = 0
    for marker in TEMPLATE_MARKERS:
        if re.search(marker, content, re.IGNORECASE | re.MULTILINE):
            hits += 1
    if hits == 0:
        return 10
    if hits == 1:
        return 6
    if hits <= 3:
        return 3
    return 0


def gate7_mermaid(content: str) -> int:
    """5 Mermaid diagrams."""
    blocks = re.findall(r'```mermaid', content)
    if len(blocks) >= 5:
        return 10
    if len(blocks) >= 3:
        return 6
    if len(blocks) >= 1:
        return 3
    return 0


def gate8_solutions(content: str) -> int:
    """10 detailed solutions — count numbered answer blocks."""
    # Count numbered items in '解答' / 'Solution' / 'Q' / numbered headings
    # Each "N." or "N)" at line start
    numbered = re.findall(r'(?:^|\n)\s*\d+[\.\)、]\s+\S', content)
    # Filter to those that are answers (not just "Q1" question)
    # If at least 10 numbered paragraphs exist anywhere, count it
    if len(numbered) >= 30:
        return 10
    if len(numbered) >= 20:
        return 7
    if len(numbered) >= 12:
        return 5
    if len(numbered) >= 6:
        return 3
    return 0


def gate9_deep_dives(content: str) -> int:
    """5 specific deep dives — recognize 深入/Deep Dive/## N. patterns."""
    # Match: "深入 N", "Deep Dive N", "## N. <name>", "### N. <name>"
    dives = re.findall(
        r'(?:深入\s*\d|Deep\s+Dive\s*[IVX\d]|##\s*\d+\.\s+\S|###\s*\d+\.\s+\S)',
        content, re.IGNORECASE
    )
    if len(dives) >= 5:
        return 5
    if len(dives) >= 3:
        return 3
    if len(dives) >= 1:
        return 1
    return 0


def gate10_no_template(content: str) -> int:
    """No T0/T1/T2 placeholders."""
    bad = re.findall(r'T\d\s*—\s*(Core|Methods|Applications)', content)
    if len(bad) == 0:
        return 5
    if len(bad) <= 2:
        return 3
    return 0


def review(file_path: str) -> dict:
    """Run all 10 gates on a file."""
    content = Path(file_path).read_text(encoding='utf-8')
    
    gates = {
        'G1_length': gate1_length(content),
        'G2_format': gate2_format(content),
        'G3_citations': gate3_citations(content),
        'G4_specificity': gate4_specificity(content),
        'G5_bilingual': gate5_bilingual(content),
        'G6_no_placeholder': gate6_no_placeholder(content),
        'G7_mermaid': gate7_mermaid(content),
        'G8_solutions': gate8_solutions(content),
        'G9_deep_dives': gate9_deep_dives(content),
        'G10_no_template': gate10_no_template(content),
    }
    total = sum(gates.values())
    
    if total >= 85:
        decision = 'APPROVED'
    elif total >= 70:
        decision = 'REVISE'
    else:
        decision = 'REJECT'
    
    return {
        'file': file_path,
        'score': total,
        'decision': decision,
        'gates': gates,
        'lines': content.count('\n'),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--course', help='single course file')
    parser.add_argument('--all', action='store_true', help='review all course files')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    
    if args.course:
        result = review(args.course)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(f"\n{result['file']}")
            print(f"  Score: {result['score']}/100  Decision: {result['decision']}")
            print(f"  Lines: {result['lines']}")
            for k, v in result['gates'].items():
                bar = '█' * v
                print(f"    {k:25s} {v:3d}/15  {bar}")
        return result['decision']
    
    if args.all:
        # Find all .md files under MIT_CEE_*
        course_files = []
        for d in os.listdir('.'):
            if d.startswith('MIT_CEE_'):
                for root, _, files in os.walk(d):
                    for f in files:
                        if f.endswith('.md') and not f.startswith('00_'):
                            course_files.append(os.path.join(root, f))
        
        results = []
        decision_count = {'APPROVED': 0, 'REVISE': 0, 'REJECT': 0}
        for f in sorted(course_files):
            r = review(f)
            results.append(r)
            decision_count[r['decision']] += 1
            if r['decision'] != 'APPROVED':
                marker = '⚠️' if r['decision'] == 'REVISE' else '❌'
                print(f"{marker} {r['score']:3d}  {f}  [{r['decision']}]")
        
        print(f"\n{'='*60}")
        print(f"Total: {len(results)} files")
        print(f"  APPROVED: {decision_count['APPROVED']}")
        print(f"  REVISE:   {decision_count['REVISE']}")
        print(f"  REJECT:   {decision_count['REJECT']}")
        
        if args.json:
            with open('_pipeline/review.json', 'w', encoding='utf-8') as fp:
                json.dump(results, fp, indent=2, ensure_ascii=False)
            print(f"\nDetailed report: _pipeline/review.json")


if __name__ == '__main__':
    main()
