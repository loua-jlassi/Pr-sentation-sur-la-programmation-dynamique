#!/usr/bin/env python3
"""
Script pour créer une version statique de la présentation
qui préserve l'apparence visuelle pour le PDF
"""

import os

def create_static_css():
    """Crée une version CSS statique pour le PDF"""
    
    static_css = """
    /* Version statique pour PDF - Désactive les animations */
    @media print {
        /* Désactiver toutes les animations */
        *, *::before, *::after {
            animation: none !important;
            transition: none !important;
            transform: none !important;
        }
        
        /* Garder les effets visuels statiques */
        .slide {
            opacity: 1 !important;
            transform: none !important;
            animation: none !important;
        }
        
        .card {
            opacity: 1 !important;
            transform: none !important;
            animation: none !important;
        }
        
        /* Préserver les couleurs et ombres */
        .slide {
            background: rgba(255, 255, 255, 0.95) !important;
            border: 2px solid rgba(70, 130, 180, 0.4) !important;
            box-shadow: 0 20px 40px rgba(70, 130, 180, 0.1) !important;
        }
        
        .card {
            background: rgba(255, 255, 255, 0.9) !important;
            border: 2px solid rgba(70, 130, 180, 0.5) !important;
            box-shadow: 0 10px 20px rgba(70, 130, 180, 0.05) !important;
        }
        
        /* Masquer les éléments flottants */
        .floating-elements {
            display: none !important;
        }
        
        .modern-nav {
            display: none !important;
        }
        
        /* Optimiser pour l'impression */
        body {
            background: white !important;
        }
        
        .slide {
            page-break-inside: avoid;
            margin: 20px 0;
        }
    }
    """
    
    return static_css

def add_static_styles_to_html():
    """Ajoute les styles statiques au fichier HTML"""
    
    html_file = "presentation_moderne_programmation_dynamique.html"
    
    if not os.path.exists(html_file):
        print(f"❌ Erreur : Le fichier {html_file} n'existe pas")
        return False
    
    # Lire le fichier HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ajouter les styles statiques avant la fermeture de </style>
    static_css = create_static_css()
    
    # Insérer les styles statiques
    if '</style>' in content:
        content = content.replace('</style>', f'{static_css}\n    </style>')
    else:
        print("❌ Erreur : Balise </style> non trouvée")
        return False
    
    # Créer une version statique
    static_file = "presentation_static_for_pdf.html"
    with open(static_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Version statique créée : {static_file}")
    return True

def create_pdf_instructions():
    """Crée un fichier d'instructions pour le PDF"""
    
    instructions = """
# 📄 INSTRUCTIONS POUR CRÉER LE PDF PARFAIT

## 🎯 Méthode Recommandée :

### 1. Utiliser la Version Statique
- Ouvrez : `presentation_static_for_pdf.html`
- Cette version préserve l'apparence sans animations

### 2. Paramètres d'Impression Optimaux
- **Format** : A4
- **Marges** : Minimales (5mm)
- **Couleurs** : Oui
- **Arrière-plans** : Oui
- **Échelle** : 100%

### 3. Étapes Détaillées
1. Ouvrir `presentation_static_for_pdf.html` dans Chrome/Safari
2. Cmd+P (ou Ctrl+P)
3. Sélectionner "Enregistrer au format PDF"
4. Ajuster les paramètres ci-dessus
5. Enregistrer

## 🎨 Ce qui sera préservé :
✅ Design moderne et professionnel
✅ Couleurs bleu foncé sur fond blanc
✅ Bordures et ombres
✅ Typographie claire
✅ Structure académique
✅ Diagrammes SVG

## ❌ Ce qui disparaîtra (normal) :
❌ Animations et transitions
❌ Effets de hover
❌ Particules flottantes
❌ Navigation interactive

## 💡 Alternative - Capture d'Écran :
Si vous voulez garder les animations, vous pouvez :
1. Ouvrir la version originale
2. Faire des captures d'écran de chaque slide
3. Créer un PDF avec les images

Votre présentation sera parfaite pour l'impression ! 🎓
"""
    
    with open("INSTRUCTIONS_PDF.md", 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("✅ Instructions créées : INSTRUCTIONS_PDF.md")

if __name__ == "__main__":
    print("🎓 CRÉATION DE LA VERSION STATIQUE POUR PDF")
    print("="*50)
    
    if add_static_styles_to_html():
        create_pdf_instructions()
        print("\n🎉 Version statique créée avec succès !")
        print("📄 Utilisez 'presentation_static_for_pdf.html' pour le PDF")
        print("📋 Consultez 'INSTRUCTIONS_PDF.md' pour les détails")
    else:
        print("❌ Erreur lors de la création de la version statique")
