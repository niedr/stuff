# Kitty Referenz

## Tab-Navigation

- **ctrl + shift + left** — Previous Tab
- **ctrl + shift + right** — Next Tab
- **ctrl + shift + .** — Tab nach vorne schieben
- **ctrl + shift + ,** — Tab nach hinten schieben
- **ctrl + shift + alt + t** — Tab-Titel setzen

## Tab Creation

- **ctrl + shift + t** — New Tab
- **ctrl + shift + q** — Tab schließen

## Window Split

- **ctrl + shift + enter** — New Window (Split)
- **ctrl + shift + w** — Close Window
- **ctrl + shift + ]** — Next Window
- **ctrl + shift + [** — Previous Window
- **ctrl + shift + l** — Next Layout (wechselt durch Layouts wie Splits, Tall, Stack, etc.)

### Split-Achse drehen (vertikal/horizontal)

- **layout_action rotate** — wechselt die Split-Achse (vertikal <-> horizontal)
  (In der Config definieren: `map ctrl+shift+r layout_action rotate`)

### Split-Layout Optionen

In der Config (`kitty.conf`):
```
enabled_layouts splits:split_axis=horizontal   # Default: nebeneinander
enabled_layouts splits:split_axis=vertical     # Alternative: übereinander
```

Layouts:
- **splits** — Flexible Splits mit freier Aufteilung
- **tall** — Links Vollhöhe, restliche Fenster rechts vertikal
- **fat** — Oben Vollbreite, restliche Fenster unten horizontal
- **grid** — Rasterartig
- **stack** — Nur ein Fenster sichtbar (wie Tabs)
- **horizontal** — Alle nebeneinander
- **vertical** — Alle untereinander

### Window-Resizing

- **ctrl + shift + r** — Resize-Modus starten (dann Pfeiltasten)
  Aus Config: `map ctrl+shift+r start_resizing_window`
- **layout_action maximize horizontal** — Fenster horizontal maximieren
- **layout_action maximize vertical** — Fenster vertikal maximieren
- **layout_action equalize** — Alle Splits gleich groß machen

### Window bewegen

- **ctrl + shift + f** — Window nach vorne (swap mit nächstem)
- **ctrl + shift + b** — Window nach hinten
- **ctrl + shift + `** — Window an die Spitze

### Focus steuern

- **ctrl + shift + 1–0** — Bestimmtes Fenster fokussieren (1 = oben links)

## Scrolling

- **ctrl + shift + up** — Zeile hoch
- **ctrl + shift + down** — Zeile runter
- **ctrl + shift + page_up** — Seite hoch
- **ctrl + shift + page_down** — Seite runter
- **ctrl + shift + home** — Ganz nach oben
- **ctrl + shift + end** — Ganz nach unten

## Shell Integration

- **ctrl + shift + g** — Ausgabe des letzten Befehls anzeigen
- **ctrl + shift + z** — Zum vorherigen Prompt springen
- **ctrl + shift + x** — Zum nächsten Prompt springen

## Schriftgröße

- **ctrl + shift + =** — Größer
- **ctrl + shift + -** — Kleiner
- **ctrl + shift + backspace** — Zurücksetzen

## URL & Text

- **ctrl + shift + e** — URL mit Tastatur öffnen (Hints)

## Copy/Paste

- **ctrl + shift + c** — Kopieren
- **ctrl + shift + v** — Einfügen (Clipboard)
- **ctrl + shift + s** — Einfügen (Selektion)
- **ctrl + shift + o** — Selektion an Programm übergeben

## Transparenz

- **ctrl + shift + a > m** — Mehr Deckkraft
- **ctrl + shift + a > l** — Weniger Deckkraft
- **ctrl + shift + a > 1** — Voll deckend
- **ctrl + shift + a > d** — Zurücksetzen

## Sonstiges

- **ctrl + shift + u** — Unicode-Zeichen eingeben
- **ctrl + shift + f11** — Fullscreen togglen
- **ctrl + shift + f10** — Maximiert togglen
- **ctrl + shift + delete** — Terminal zurücksetzen
- **ctrl + shift + f5** — Config neu laden
- **ctrl + shift + f2** — Config-Datei editieren
- **ctrl + shift + f1** — Kitty-Doku im Browser
- **ctrl + shift + escape** — Kitty Shell (zum Steuern per Kommando)
- **ctrl + shift + h** — Scrollback im Pager anzeigen

## Config

Pfad: `~/.config/kitty/kitty.conf`
