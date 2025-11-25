import os

def fix_file(filepath):
    """Fix imports in a Python file"""
    if not os.path.exists(filepath):
        print(f"⚠️  {filepath} not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Backup
    with open(filepath + '.backup', 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Fix imports
    replacements = {
        'from langchain.embeddings import': 'from langchain_community.embeddings import',
        'from langchain.llms import': 'from langchain_community.llms import',
        'from langchain.vectorstores import': 'from langchain_community.vectorstores import',
        'from langchain.document_loaders import': 'from langchain_community.document_loaders import',
    }
    
    fixed = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            print(f"✅ Fixed in {filepath}: {old}")
            fixed = True
    
    if fixed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ {filepath} fixed! Backup: {filepath}.backup")
    else:
        print(f"✅ {filepath} already correct")

# Fix all files
print("🔧 Fixing imports...\n")
fix_file('src/helper.py')
fix_file('src/hf_llm.py')
fix_file('store_index.py')  # If you have this
print("\n✅ Done! Try running app.py now")