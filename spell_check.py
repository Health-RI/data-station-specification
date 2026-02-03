#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Spell checker for markdown documentation."""

import re
from pathlib import Path
from spellchecker import SpellChecker

spell_en = SpellChecker(language='en')
spell_nl = SpellChecker(language='nl')

IGNORE_WORDS = {
    'mkdocs', 'yml', 'md', 'toml', 'bib', 'css', 'html', 'json', 'xml', 'csv',
    'pyproject', 'justfile', 'github', 'git', 'api', 'apis', 'http', 'https',
    'url', 'urls', 'uri', 'uris',
    'daams', 'hdab', 'tehdas', 'kik', 'datashield', 'plugin', 'datastation',
    'datastations', 'mdw', 'spe',
    'federatief', 'federatieve', 'hoeksteen', 'leeswijzer', 'woordenlijst',
    'waarom', 'discussie', 'implementaties', 'analyseren', 'aanvragen',
    'klaarzetten', 'publiceren', 'vinden', 'syntactisch', 'semantisch',
    'centraal', 'decentraal', 'ontwikkelagenda', 'primair', 'secundair',
    'catalogus', 'pooling', 'leren', 'analyse', 'applicatie', 'infrastructuur',
    'proces', 'informatie', 'standaarden', 'als', 'vs', 'een', 'het', 'de',
    'van', 'voor', 'en', 'bij', 'op', 'aan', 'met', 'worden', 'zijn',
    'hebben', 'kunnen', 'moeten', 'zullen', 'mogen', 'naar', 'uit', 'over',
    'onder', 'tussen', 'door', 'bij', 'tot', 'vanaf', 'binnen', 'buiten',
}


def extract_words_from_markdown(content):
    """Extract words from markdown content, filtering out code and markup."""
    content = re.sub(r'```[^`]*```', '', content)
    content = re.sub(r'`[^`]+`', '', content)
    content = re.sub(r'https?://\S+', '', content)
    content = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'\1', content)
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
    content = re.sub(r'<[^>]+>', '', content)
    content = re.sub(r'^#+\s+', '', content, flags=re.MULTILINE)
    words = re.findall(r'\b[a-zA-ZàáâäãåèéêëìíîïòóôöõøùúûüýÿñçčšžÀÁÂÄÃÅÈÉÊËÌÍÎÏÒÓÔÖÕØÙÚÛÜÝŸÑßÇŒÆČŠŽ∂ð]+\b', content)
    return [w.lower() for w in words if len(w) > 2]


def check_file(file_path):
    """Check spelling in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return None, f"Error reading file: {e}"
    
    words = extract_words_from_markdown(content)
    if not words:
        return {}, None
    
    is_english = '.en.md' in str(file_path)
    spell = spell_en if is_english else spell_nl
    
    unique_words = set(words)
    misspelled = {w for w in unique_words if w not in IGNORE_WORDS}
    misspelled = spell.unknown(misspelled)
    
    if not misspelled:
        return {}, None
    
    errors = {word: [] for word in sorted(misspelled)}
    
    return errors, None


def main():
    """Main spell checking function."""
    docs_path = Path('docs')
    includes_path = Path('includes')
    
    md_files = []
    if docs_path.exists():
        md_files.extend(docs_path.rglob('*.md'))
    if includes_path.exists():
        md_files.extend(includes_path.rglob('*.md'))
    
    print(f'Checking {len(md_files)} markdown files...\n')
    
    files_with_errors = {}
    files_with_issues = []
    
    for i, md_file in enumerate(sorted(md_files), 1):
        print(f'[{i}/{len(md_files)}] Checking {md_file}...', end=' ')
        errors, issue = check_file(md_file)
        
        if issue:
            print(f'⚠️  {issue}')
            files_with_issues.append((str(md_file), issue))
        elif errors:
            print(f'❌ {len(errors)} issues')
            files_with_errors[str(md_file)] = errors
        else:
            print('✅')
    
    print('\n' + '='*70)
    print('SPELL CHECK RESULTS')
    print('='*70)
    
    if files_with_errors:
        print(f'\n📝 Found spelling issues in {len(files_with_errors)} files:\n')
        for file_path, errors in sorted(files_with_errors.items()):
            print(f'\n{file_path}:')
            for word, suggestions in sorted(errors.items())[:20]:
                if suggestions:
                    print(f'  • "{word}" → {", ".join(suggestions)}')
                else:
                    print(f'  • "{word}" (no suggestions)')
    else:
        print('\n✅ No spelling errors found!')
    
    if files_with_issues:
        print(f'\n⚠️  Issues reading {len(files_with_issues)} files:')
        for file_path, issue in files_with_issues:
            print(f'  • {file_path}: {issue}')
    
    print(f'\nTotal files checked: {len(md_files)}')
    print(f'Files with spelling errors: {len(files_with_errors)}')


if __name__ == '__main__':
    main()
