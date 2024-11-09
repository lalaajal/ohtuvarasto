from varasto import Varasto




def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print1(mehua, olutta)

    print(f"Olutvarasto: {olutta}\nolutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}\nMehuvarasto: {mehua}\n \
          mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

    print(f"Olutvarasto: {olutta}\nolutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}\nOlutvarasto: {olutta}")
    print(f"Mehuvarasto: {mehua}\nmehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}\nMehuvarasto: {mehua}")

def print1(mehua, olutta):
    print(f"Luonnin jälkeen:\nMehuvarasto: {mehua}\nOlutvarasto: {olutta}\n" \
          "Olut getterit:\nsaldo = {olutta.saldo}\n" \
          "tilavuus = {olutta.tilavuus}\npaljonko_mahtuu =" \
          " {olutta.paljonko_mahtuu()}\nMehu setterit:Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}\nVirhetilanteita:\nVarasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

if __name__ == "__main__":
    main()
