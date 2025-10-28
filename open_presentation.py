#!/usr/bin/env python3
"""
Script pour ouvrir la présentation dans le navigateur
pour faciliter la conversion en PDF
"""

import webbrowser
import os
import sys

def open_presentation():
    """Ouvre la présentation dans le navigateur par défaut"""
    
    html_file = "presentation_moderne_programmation_dynamique.html"
    
    if not os.path.exists(html_file):
        print(f"❌ Erreur : Le fichier {html_file} n'existe pas")
        return False
    
    # Chemin absolu du fichier
    file_path = os.path.abspath(html_file)
    file_url = f"file://{file_path}"
    
    print("🎓 OUVERTURE DE LA PRÉSENTATION")
    print("="*40)
    print(f"📄 Fichier : {html_file}")
    print(f"🌐 URL : {file_url}")
    print("\n📋 INSTRUCTIONS POUR CONVERTIR EN PDF :")
    print("1. La présentation s'ouvre dans votre navigateur")
    print("2. Appuyez sur Cmd+P (Mac) ou Ctrl+P (Windows)")
    print("3. Sélectionnez 'Enregistrer au format PDF'")
    print("4. Ajustez les paramètres :")
    print("   - Format : A4")
    print("   - Marges : Minimales")
    print("   - Couleurs : Oui")
    print("   - Arrière-plans : Oui")
    print("5. Cliquez sur 'Enregistrer'")
    print("\n✨ Votre PDF sera prêt !")
    
    # Ouvrir dans le navigateur
    webbrowser.open(file_url)
    return True

if __name__ == "__main__":
    if open_presentation():
        print("\n🎉 Présentation ouverte dans le navigateur !")
        print("📄 Suivez les instructions ci-dessus pour créer le PDF")
    else:
        print("❌ Impossible d'ouvrir la présentation")
