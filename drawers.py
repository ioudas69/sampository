def lades():
    rechts = int(input("recht lades per stuk: "))
    links = int(input("links lades per stuk: "))
    
    totaal_lades = rechts + links
    
    print(f"U hebt totaal {totaal_lades} st gekozen")
    return(totaal_lades)

if __name__ == "__main__":
    lades()