import drawers as drawers

def maken_kast():
    uurtarief = 45

    antaal_stuk = drawers.lades()
    

    print(f"Gaat {antaal_stuk*uurtarief} € kosten")
    
if __name__ == "__main__":
    maken_kast()
