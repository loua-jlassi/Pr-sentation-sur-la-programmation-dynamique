#!/usr/bin/env python3
"""
Script pour convertir la présentation HTML en PDF
Utilise wkhtmltopdf pour une conversion de haute qualité
"""

import subprocess
import os
import sys

def convert_html_to_pdf():
    """Convertit le fichier HTML en PDF"""
    
    html_file = "presentation_moderne_programmation_dynamique.html"
    pdf_file = "Programmation_Dynamique_Presentation.pdf"
    
    # Vérifier si le fichier HTML existe
    if not os.path.exists(html_file):
        print(f"❌ Erreur : Le fichier {html_file} n'existe pas")
        return False
    
    try:
        # Commande wkhtmltopdf avec options optimisées
        cmd = [
            "wkhtmltopdf",
            "--page-size", "A4",
            "--orientation", "Portrait",
            "--margin-top", "10mm",
            "--margin-bottom", "10mm",
            "--margin-left", "10mm",
            "--margin-right", "10mm",
            "--encoding", "UTF-8",
            "--enable-local-file-access",
            "--print-media-type",
            "--disable-smart-shrinking",
            "--zoom", "1.0",
            html_file,
            pdf_file
        ]
        
        print("🔄 Conversion en cours...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Conversion réussie !")
            print(f"📄 PDF créé : {pdf_file}")
            print(f"📊 Taille : {os.path.getsize(pdf_file)} bytes")
            return True
        else:
            print(f"❌ Erreur lors de la conversion :")
            print(result.stderr)
            return False
            
    except FileNotFoundError:
        print("❌ wkhtmltopdf n'est pas installé")
        print("📥 Installation nécessaire :")
        print("   - Ubuntu/Debian: sudo apt-get install wkhtmltopdf")
        print("   - macOS: brew install wkhtmltopdf")
        print("   - Windows: Télécharger depuis https://wkhtmltopdf.org/")
        return False
    except Exception as e:
        print(f"❌ Erreur : {e}")
        return False

def install_wkhtmltopdf_instructions():
    """Affiche les instructions d'installation"""
    print("\n" + "="*60)
    print("📥 INSTRUCTIONS D'INSTALLATION WKHTMLTOPDF")
    print("="*60)
    
    print("\n🖥️  UBUNTU/DEBIAN:")
    print("sudo apt-get update")
    print("sudo apt-get install wkhtmltopdf")
    
    print("\n🍎 MACOS:")
    print("brew install wkhtmltopdf")
    
    print("\n🪟 WINDOWS:")
    print("1. Télécharger depuis: https://wkhtmltopdf.org/downloads.html")
    print("2. Installer l'exécutable")
    print("3. Ajouter au PATH système")
    
    print("\n🐧 ALTERNATIVE - Utiliser le navigateur:")
    print("1. Ouvrir le fichier HTML dans Chrome/Firefox")
    print("2. Ctrl+P (ou Cmd+P)")
    print("3. Sélectionner 'Enregistrer au format PDF'")
    print("4. Ajuster les paramètres et sauvegarder")

if __name__ == "__main__":
    print("🎓 CONVERTISSEUR HTML VERS PDF")
    print("="*40)
    
    if convert_html_to_pdf():
        print("\n🎉 Votre présentation est maintenant en PDF !")
    else:
        install_wkhtmltopdf_instructions()
