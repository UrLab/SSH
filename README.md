# SSH
Simplified Stock Handler

ça fait un petit moment qu'il n'y avait rien qui affichait les prix des denrées alimentaires dans la cuisine. Changeons ça!

S.S.H est un raspberry pi 3b+, un écran tactile et un scanner de code barre permettant de connaitre le prix des produits au hackerspace.

## à propos de l'écran tactile:
Il s'agit d'un écran de la marque Innolux.
[la datasheet de l'écran][1]
L'écran est controlé par  un controleur LCD VS-TY2662-V1 dont [voici la datasheet][2]. Il est accompagné d'un "clavier"([datasheet pas très fournie][3]).
La partie tactile est controlée par un ETP-4500UG-X
[cette page parle des etp-4500ug][4] et à un lien pour [télécharger les drivers dont le contrôleur a besoin][5]

[1]: http://www.bdtic.com/datasheet/Innolux/AT070TNA2-V1.pdf "datasheet de l'écran"
[2]: http://www.vslcd.com/Specification/VS-TY2662-V1.pdf "datasheet contrôleur LCD"
[3]: https://cdn-shop.adafruit.com/datasheets/PCB800023+Keyboard.pdf "datasheet du clavier du contrôleur LCD"
[4]: https://www.short-circuit.com/product/etp-4500ug.html "etp-4500ug"
[5]: https://www.short-circuit.com/support/drivers.html "etp-4500ug drivers"
