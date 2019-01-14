---
id: 241
title: SIG collaboratif, solution simple et gratuite
date: 2018-05-23T16:47:03+00:00
author: Zoran
layout: post
guid: https://landscapearchaeology.org/?p=241
permalink: /2018/postgis-hosting-fr/
categories:
  - 'Spatial analysis &amp; GIS'
---
Travailler, ce n’est peut-être pas toujours la chose la plus passionnante, mais c’est quand même plus amusant (et plus efficace) en collaboration. Il y a, dans le monde du SIG, bien de solutions pour le travail collaboratif sur un même jeu de données, mais le plus souvent elles sont coûteuses ou exigeantes au niveau technique.

Cependant, il existe un moyen quelque peu obscur, caché dans le benthos de l’internet, qui permet d’utiliser l’architecture collaborative – gratuitement. Le hébergeur <a href="http://www.alwaysdata.com">Alwaysdata</a> (la compagnie est française malgré le nom) offre dans son paquet découverte l’hébergement des bases de données PostGIS, très performantes et largement utilisées dans le monde SIG.

Nous verrons maintenant comment aborder le problème le plus basique : créer une base de données en ligne pour s’y connecter par la suite.

1) D’abord il faut créer un compte sur le site d’<a href="https://www.alwaysdata.com">Awaysdata</a> et ajouter par la suite une base de données PostgreSQL (dans le tableau de bord, choisir <em>Bases de données -> PostgreSQL</em>). Renseignez le nom de la base, et surtout cochez la case PostGIS (ce dernier étant une extension de PostgreSQL).

<img src="https://3.bp.blogspot.com/-ILewq8u2xjo/Wgc4hQjFeGI/AAAAAAAAA3Y/ETSfd78twOAI5e59-mAiyrSLhZXoqbtcwCEwYBhgL/s1600/alwaysdata1.jpg" alt="" />

2) Ensuite, il faut ajouter un/des utilisateurs et renseigner le/les mots de passe (toujours dans la même rubrique « <em>Bases de données » PostgreSQL</em> »). Pour l’utilisateur-propriétaire, le mot de passe est le même que pour le compte même (sauf si spécifié autrement).

<img src="https://2.bp.blogspot.com/-2O81PYVwyfI/Wgc4hvhUMpI/AAAAAAAAA3c/MRLGUBgtr1I6JfhBqA_lnG5BgqtLOATdQCEwYBhgL/s1600/alwaysdata2.jpg" alt="" />

3) Enfin le dernier élément, l’adresse internet de notre base. Celle-ci sera affichée après la création de la base et devrait ressembler à « postgresql-NOM&#95;DE&#95;INSCRIPTION.awaysdata.net ». Notez-la.

<img src="https://4.bp.blogspot.com/-SDAz6Jj3qP4/Wgc4iKyOzAI/AAAAAAAAA3g/zNWVL3FtFwoGOhXs7FePqkHjb7QLmKp0wCEwYBhgL/s1600/alwaysdata3.jpg" alt="" />

Nous disposons maintenant de quatre informations nécessaires : adresse de la base, son nom et le nom d’utilisateur avec son mot de passe. Je passerai maintenant au QGIS pour faire marcher l’engin. Il s’agit tout simplement d’une connexion à la base de données, ce qui devrait être faisable par n’importe quel logiciel SIG digne de ce nom.

a) Approche directe : Ajouter une couche PostGIS. Choisir une nouvelle connexion et remplir les cases avec nos informations.

<img src="https://4.bp.blogspot.com/-aSSUh2iNjCk/Wgc4g52MNJI/AAAAAAAAA3Q/g9m1tsyw3s8CSrnqf6B9DCR0BhJObti-wCEwYBhgL/s1600/QGIS1.jpg" alt="" />

Ensuite, dans <em>Database » Manager</em> utiliser la fonction Import layer pour ajouter les données (parce que la base est vide …)

b) Approche « comme il faut ». On devrait plutôt gérer nos sources de données dans le QGIS Browser, c’est plus propre. Donc, tout simplement, créer une connexion en renseignant les mêmes informations que dessus (laissez vide la case « service »). Passez, ensuite, dans le QGIS et ajoutez la couche PostGIS depuis cette connexion.

<img src="https://2.bp.blogspot.com/-BP60yCMS9i0/Wgc4hC94feI/AAAAAAAAA3o/6B9uRWCT0z8eFG8qstK9VzpV5yQXAKxrwCEwYBhgL/s1600/QGIS2.jpg" alt="" />

Et voilà, une solution « pro » ! PostGIS est capable de gérer <em>des centaines</em> d’utilisateurs, donc pas de souci au niveau de software. Pour des usages avancés, vous avez l’accès direct à la base PostGIS via l’adresse <a href="https://phppgadmin.alwaysdata.com/">phppgadmin.alwaysdata.com</a>. (C’est le sujet pour une autre occasion…)

<h3>Bémol (il y en toujours un…)</h3>

La solution décrite ici utilise un paquet promotionnel : aucune obligation particulière n’est impliquée de part de l’hébergeur (si j’ai bien compris). En effet, le compte, <em>avec tous les données</em> sera d’abord suspendu dans le cas d’une période d’inactivité supérieure à deux mois, pour se faire carrément <em>effacer</em> suite à 30 jours supplémentaires (au moins c’est mon expérience). La taille de l’hébergement entier est limité à 100 mb : cela devrait souffrir pour une utilisation plutôt légère, mais probablement pas pour des projets d’envergure. Il s’agit, en fin de compte, d’un paquet gratuit, promotionnel, avec des fonctionnalités assez avancées (notamment au niveau d’installation de PostGIS) : on ne devrait pas critiquer, c’est déjà pas mal ! Investissez quelques sous pour un travail plus sérieux… (Je n’ai aucun lien avec la compagnie.)

Enfin, restent tous les problèmes d’organisation d’une base collective. Par exemple, qu’est-ce qu’il se passe quand plusieurs utilisateurs tentent de modifier les données en même temps ? Sans un paramétrage supplémentaire, c’est le plus rapide qui gagne. Mais, c’est le problème pour une autre occasion… <a href="http://workshops.boundlessgeo.com/postgis-intro/history_tracking.html">(voir ici, par exemple)</a>