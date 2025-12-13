# Izračun za 2, 3, 5, 7 in 8 let (24, 36, 60, 84, 96 mesecev) pri 15.000 € pologa

scenariji = [24, 36, 60, 84, 96]
rezultati = []

for m in scenariji:
    placano = obrok * m
    ostanek = preostanek_glavnice(znesek_financiranja, obrok, obrestna_mera, meseci, m)
    if m == 96:  # konec
        skupaj = placano + polog
    else:
        skupaj = placano + ostanek + polog
    rezultati.append({
        "Obdobje": f"{m//12} let",
        "Plačani obroki (€)": round(placano, 2),
        "Preostanek glavnice (€)": round(ostanek, 2) if m < 96 else 0,
        "Skupaj plačano (€)": round(skupaj, 2)
    })

df_all = pd.DataFrame(rezultati)
caas_jupyter_tools.display_dataframe_to_user("Tabela stroškov leasinga (15.000 € pologa, 2–8 let)", df_all)
