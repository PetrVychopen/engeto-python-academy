import re

def extract_municipality_code(html_text):
    # Define the regex pattern to find the municipality code
    pattern = r'XOBEC=(\d+)'

    # Search for the pattern in the HTML text
    match = re.search(pattern, html_text)

    if match:
        # Extract the municipality code from the matched group
        municipality_code = match.group(1)
        return municipality_code
    else:
        # Return None if the municipality code is not found
        return None

# Example usage
html_content = """

<!doctype html>
<html lang="cs">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<link rel="stylesheet" type="text/css" href="styly" media="screen, print">
<title>Výsledky hlasování za územní celky | volby.cz</title>
</head>
<body>
<header>
<div id="header2">
<div class="in_1020">
<div id="header_1020">
<a href="/" id="logo"><span>volby.cz</span></a>
<span id="headerLinkvolby">www.volby.cz</span>
<a href="https://www.czso.cz/csu/czso/domov" id="csu_logo"><span>Český statistický úřad</span></a>
<span id="headerLink">www.czso.cz</span>
</div> <!-- header end -->
<div class="clear"></div>
<nav aria-label="Drobečková navigace">
<p class="drobek">
<a href="/"><span></span> Úvod</a> > <a href="ps?xjazyk=CZ">Poslanecká sněmovna 2017</a> > <a href="ps3?xjazyk=CZ">Výsledky hlasování &ndash; výběr územní úrovně</a> > <a href="ps32?xjazyk=CZ&amp;xkraj=12&amp;xnumnuts=7103">Okres&nbsp;Prostějov &ndash; výběr obce</a> > Obec&nbsp;Alojzov
</p>
<!--drobeckova navigace-->
</nav>
<h1>
Volby do Poslanecké sněmovny Parlamentu České republiky konané ve dnech 20.10. &ndash; 21.10.2017 (promítnuto usnesení NSS)
</h1>
</div>
</div> <!-- header2 end -->
</header>
<main>
<div id="container">
<div class="in_1020">
<div id="core">
<div id="content">
<div id="publikace" class="topline">
<h2>
Výsledky hlasování za územní celky
</h2>
<h3>
Kraj: Olomoucký kraj
</h3>
<h3>
Okres: Prostějov
</h3>
<h3>
Obec: Alojzov
</h3>
<table id="ps311_t1" class="table">
<tr>
<th colspan="3" id="sa1">Okrsky</th>
<th rowspan="2" id="sa2" data-rel="L1">Voliči<br>v seznamu</th>
<th rowspan="2" id="sa3" data-rel="L1">Vydané<br>obálky</th>
<th rowspan="2" id="sa4">Volební<br>účast v %</th>
<th rowspan="2" id="sa5" data-rel="L1">Odevzdané<br>obálky</th>
<th rowspan="2" id="sa6" data-rel="L1">Platné<br>hlasy</th>
<th rowspan="2" id="sa7">% platných<br>hlasů</th>
</tr>
<tr>
<th id="sb1">celkem</th>
<th id="sb2">zpr.</th>
<th id="sb3">v %</th>
</tr>
<tr>
<td class="cislo" headers="sa1 sb1">1</td>
<td class="cislo" headers="sa1 sb2">1</td>
<td class="cislo" headers="sa1 sb3">100,00</td>
<td class="cislo" headers="sa2" data-rel="L1">205</td>
<td class="cislo" headers="sa3" data-rel="L1">145</td>
<td class="cislo" headers="sa4">70,73</td>
<td class="cislo" headers="sa5" data-rel="L1">145</td>
<td class="cislo" headers="sa6" data-rel="L1">144</td>
<td class="cislo" headers="sa7">99,31</td>
</tr>
</table>
<div class="tab_full_ps311">
<a href="ps311?XJAZYK=CZ&XKRAJ=12&XOBEC=506761&XVYBER=7103&amp;xf=1">úplné zobrazení</a>
</div>
<div id="outer">
<div id="inner">
<div class="t2_470">
<h3 class="skryto">
Výsledky hlasování za územní celky &ndash; Obec&nbsp;Alojzov &ndash; část 1
</h3>
<details class="skryto">
<summary>
Popis tabulky
</summary>
Tabulka umožňuje výběr příslušného územního celku na úrovni okresů. K výběru případných dalších územních celků použijte odkazy označené symbolem X.
</details>
<table class="table">
<tr>
<th colspan="2" id="t1sa1">Strana</th>
<th colspan="2" id="t1sa2">Platné hlasy</th>
<th rowspan="2" id="t1sa3">Předn.<br>hlasy</th>
</tr>
<tr>
<th id="t1sb1">číslo</th>
<th class="fixed200" id="t1sb2">název</th>
<th id="t1sb3">celkem</th>
<th id="t1sb4">v %</th>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">1</td>
<td class="overflow_name" headers="t1sa1 t1sb2">Občanská demokratická strana</td>
<td class="cislo" headers="t1sa2 t1sb3">29</td>
<td class="cislo" headers="t1sa2 t1sb4">20,13</td>
<td class="center" headers="t1sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=1">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">2</td>
<td class="overflow_name" headers="t1sa1 t1sb2">Řád národa - Vlastenecká unie</td>
<td class="cislo" headers="t1sa2 t1sb3">0</td>
<td class="cislo" headers="t1sa2 t1sb4">0,00</td>
<td class="hidden_td" headers="t1sa3">-</td>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">3</td>
<td class="overflow_name" headers="t1sa1 t1sb2">CESTA ODPOVĚDNÉ SPOLEČNOSTI</td>
<td class="cislo" headers="t1sa2 t1sb3">0</td>
<td class="cislo" headers="t1sa2 t1sb4">0,00</td>
<td class="hidden_td" headers="t1sa3">-</td>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">4</td>
<td class="overflow_name" headers="t1sa1 t1sb2">Česká str.sociálně demokrat.</td>
<td class="cislo" headers="t1sa2 t1sb3">9</td>
<td class="cislo" headers="t1sa2 t1sb4">6,25</td>
<td class="center" headers="t1sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=4">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">6</td>
<td class="overflow_name" headers="t1sa1 t1sb2">Radostné Česko</td>
<td class="cislo" headers="t1sa2 t1sb3">0</td>
<td class="cislo" headers="t1sa2 t1sb4">0,00</td>
<td class="hidden_td" headers="t1sa3">-</td>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">7</td>
<td class="overflow_name" headers="t1sa1 t1sb2">STAROSTOVÉ A NEZÁVISLÍ</td>
<td class="cislo" headers="t1sa2 t1sb3">5</td>
<td class="cislo" headers="t1sa2 t1sb4">3,47</td>
<td class="center" headers="t1sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=7">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">8</td>
<td class="overflow_name" headers="t1sa1 t1sb2">Komunistická str.Čech a Moravy</td>
<td class="cislo" headers="t1sa2 t1sb3">17</td>
<td class="cislo" headers="t1sa2 t1sb4">11,80</td>
<td class="center" headers="t1sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=8">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">9</td>
<td class="overflow_name" headers="t1sa1 t1sb2">Strana zelených</td>
<td class="cislo" headers="t1sa2 t1sb3">4</td>
<td class="cislo" headers="t1sa2 t1sb4">2,77</td>
<td class="center" headers="t1sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=9">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">10</td>
<td class="overflow_name" headers="t1sa1 t1sb2">ROZUMNÍ-stop migraci,diktát.EU</td>
<td class="cislo" headers="t1sa2 t1sb3">1</td>
<td class="cislo" headers="t1sa2 t1sb4">0,69</td>
<td class="center" headers="t1sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=10">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">12</td>
<td class="overflow_name" headers="t1sa1 t1sb2">Strana svobodných občanů</td>
<td class="cislo" headers="t1sa2 t1sb3">1</td>
<td class="cislo" headers="t1sa2 t1sb4">0,69</td>
<td class="center" headers="t1sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=12">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">13</td>
<td class="overflow_name" headers="t1sa1 t1sb2">Blok proti islam.-Obran.domova</td>
<td class="cislo" headers="t1sa2 t1sb3">0</td>
<td class="cislo" headers="t1sa2 t1sb4">0,00</td>
<td class="hidden_td" headers="t1sa3">-</td>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">14</td>
<td class="overflow_name" headers="t1sa1 t1sb2">Občanská demokratická aliance</td>
<td class="cislo" headers="t1sa2 t1sb3">0</td>
<td class="cislo" headers="t1sa2 t1sb4">0,00</td>
<td class="hidden_td" headers="t1sa3">-</td>
</tr>
<tr>
<td class="cislo" headers="t1sa1 t1sb1">15</td>
<td class="overflow_name" headers="t1sa1 t1sb2">Česká pirátská strana</td>
<td class="cislo" headers="t1sa2 t1sb3">18</td>
<td class="cislo" headers="t1sa2 t1sb4">12,50</td>
<td class="center" headers="t1sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=15">X</a></td>
</tr>
</table>
</div>
<div class="t2_470">
<h3 class="skryto">
Výsledky hlasování za územní celky &ndash; Obec&nbsp;Alojzov &ndash; část 2
</h3>
<details class="skryto">
<summary>
Popis tabulky
</summary>
Tabulka umožňuje výběr příslušného územního celku na úrovni okresů. K výběru případných dalších územních celků použijte odkazy označené symbolem X.
</details>
<table class="table">
<tr>
<th colspan="2" id="t2sa1">Strana</th>
<th colspan="2" id="t2sa2">Platné hlasy</th>
<th rowspan="2" id="t2sa3">Předn.<br>hlasy</th>
</tr>
<tr>
<th id="t2sb1">číslo</th>
<th class="fixed200" id="t2sb2">název</th>
<th id="t2sb3">celkem</th>
<th id="t2sb4">v %</th>
</tr>
<tr>
<td class="cislo" headers="t2sa1 t2sb1">19</td>
<td class="overflow_name" headers="t2sa1 t2sb2">Referendum o Evropské unii</td>
<td class="cislo" headers="t2sa2 t2sb3">0</td>
<td class="cislo" headers="t2sa2 t2sb4">0,00</td>
<td class="hidden_td" headers="t2sa3">-</td>
</tr>
<tr>
<td class="cislo" headers="t2sa1 t2sb1">20</td>
<td class="overflow_name" headers="t2sa1 t2sb2">TOP 09</td>
<td class="cislo" headers="t2sa2 t2sb3">5</td>
<td class="cislo" headers="t2sa2 t2sb4">3,47</td>
<td class="center" headers="t2sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=20">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t2sa1 t2sb1">21</td>
<td class="overflow_name" headers="t2sa1 t2sb2">ANO 2011</td>
<td class="cislo" headers="t2sa2 t2sb3">32</td>
<td class="cislo" headers="t2sa2 t2sb4">22,22</td>
<td class="center" headers="t2sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=21">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t2sa1 t2sb1">22</td>
<td class="overflow_name" headers="t2sa1 t2sb2">Dobrá volba 2016</td>
<td class="cislo" headers="t2sa2 t2sb3">0</td>
<td class="cislo" headers="t2sa2 t2sb4">0,00</td>
<td class="hidden_td" headers="t2sa3">-</td>
</tr>
<tr>
<td class="cislo" headers="t2sa1 t2sb1">23</td>
<td class="overflow_name" headers="t2sa1 t2sb2">SPR-Republ.str.Čsl. M.Sládka</td>
<td class="cislo" headers="t2sa2 t2sb3">0</td>
<td class="cislo" headers="t2sa2 t2sb4">0,00</td>
<td class="hidden_td" headers="t2sa3">-</td>
</tr>
<tr>
<td class="cislo" headers="t2sa1 t2sb1">24</td>
<td class="overflow_name" headers="t2sa1 t2sb2">Křesť.demokr.unie-Čs.str.lid.</td>
<td class="cislo" headers="t2sa2 t2sb3">6</td>
<td class="cislo" headers="t2sa2 t2sb4">4,16</td>
<td class="center" headers="t2sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=24">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t2sa1 t2sb1">25</td>
<td class="overflow_name" headers="t2sa1 t2sb2">Česká strana národně sociální</td>
<td class="cislo" headers="t2sa2 t2sb3">0</td>
<td class="cislo" headers="t2sa2 t2sb4">0,00</td>
<td class="hidden_td" headers="t2sa3">-</td>
</tr>
<tr>
<td class="cislo" headers="t2sa1 t2sb1">26</td>
<td class="overflow_name" headers="t2sa1 t2sb2">REALISTÉ</td>
<td class="cislo" headers="t2sa2 t2sb3">0</td>
<td class="cislo" headers="t2sa2 t2sb4">0,00</td>
<td class="hidden_td" headers="t2sa3">-</td>
</tr>
<tr>
<td class="cislo" headers="t2sa1 t2sb1">27</td>
<td class="overflow_name" headers="t2sa1 t2sb2">SPORTOVCI</td>
<td class="cislo" headers="t2sa2 t2sb3">1</td>
<td class="cislo" headers="t2sa2 t2sb4">0,69</td>
<td class="center" headers="t2sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=27">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t2sa1 t2sb1">28</td>
<td class="overflow_name" headers="t2sa1 t2sb2">Dělnic.str.sociální spravedl.</td>
<td class="cislo" headers="t2sa2 t2sb3">1</td>
<td class="cislo" headers="t2sa2 t2sb4">0,69</td>
<td class="center" headers="t2sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=28">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t2sa1 t2sb1">29</td>
<td class="overflow_name" headers="t2sa1 t2sb2">Svob.a př.dem.-T.Okamura (SPD)</td>
<td class="cislo" headers="t2sa2 t2sb3">15</td>
<td class="cislo" headers="t2sa2 t2sb4">10,41</td>
<td class="center" headers="t2sa3"><a href="ps351?xjazyk=CZ&amp;xkraj=12&amp;xobec=506761&amp;xvyber=7103&amp;xstrana=29">X</a></td>
</tr>
<tr>
<td class="cislo" headers="t2sa1 t2sb1">30</td>
<td class="overflow_name" headers="t2sa1 t2sb2">Strana Práv Občanů</td>
<td class="cislo" headers="t2sa2 t2sb3">0</td>
<td class="cislo" headers="t2sa2 t2sb4">0,00</td>
<td class="hidden_td" headers="t2sa3">-</td>
</tr>
<tr>
<td class="hidden_td" headers="t2sa1 t2sb1">-</td>
<td class="hidden_td" headers="t2sa1 t2sb2">-</td>
<td class="hidden_td" headers="t2sa2 t2sb3">-</td>
<td class="hidden_td" headers="t2sa2 t2sb4">-</td>
<td class="hidden_td" headers="t2sa3">-</td>
</tr>
</table>
</div>
</div>
</div>
<div class="clear"></div>
<nav aria-label="O úroveň výš">
<p class="drobek_back">
Zpět: <a href="ps32?xjazyk=CZ&amp;xkraj=12&amp;xnumnuts=7103">Okres&nbsp;Prostějov &ndash; výběr obce</a>
</p>
<!--drobeckova navigace-->
</nav>
</div><!-- end publikace-->
</div><!-- end content-->
</div> <!-- core end -->
</div> <!-- in end -->
</div> <!-- container end -->
</main>
<footer>
<div id="footer">
<div class="in_1020">
<div class="footerContent">
<ul>
<li>&copy; Český statistický úřad, 2021</li>
<li><a href="/cz/prohlaseni_o_pristupnosti.htm">Prohlášení o přístupnosti</a></li>
<li>Datum a čas generování stránky:&nbsp; 06/03/2024 19:33:24</li>
</ul>
</div>
</div>
</div> <!-- footer end -->
</footer>
</body>
</html>
"""

code = extract_municipality_code(html_content)
print(code)
