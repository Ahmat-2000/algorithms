/**
 * @file file_priorite.h
 * @author Cours M1 Structures de données avancées
 * */

#ifndef __FILE_PRIORITE__H__
#define __FILE_PRIORITE__H__

#include <stdlib.h>
#include "liste.h"
#include <stdbool.h>


/**
 * @brief Structure encodant un tas binaire.
 * On va ici travailler avec un tas binaire "minimum".
 * Toutefois, si on souhaite travailler avec un tas binaire "maximum",
 * on peut changer le champ "est_plus_petit" (fonction de comparaison).
 */
struct TasBinaire {
	
	Liste valeurs; 	 /**< Une liste qui va contenir les différentes valeurs*/
	
	bool (*est_plus_petit) (type_base,type_base); /**< Un pointeur vers la 
	fonction qui indique si l'élément 1 est plus petit que l'élement 2. \n
	Si jamais on voulait un tas binaire max, on pourrait mettre ici un pointeur
	vers une fonction 
	`bool est_plus_grand(type_base x, type_base y){ return (x >= y); }`. 
	(En gros on inverse l'ordre.)*/
									
};


/**
 * @brief On implémente les files de priorités (minimum) comme pointeurs vers des tas binaires.
 */
typedef struct TasBinaire* FilePriorite;


/* Prototype des fonctions */


/**
 * @brief La fonction qui, normalement, compare deux éléments entre eux.
 * Son adresse remplira par défaut le champ ̀`est_plus_petit̀` de notre structure.
 * Ici on renverra tout simplement `x < y`.
 * Si le "type de base" est différent, ou si on veut tout le temps avoir des tas
 * max, on changera cette fonction.
 * @param x, un élément de base, 
 * @param y, un élément de base.
 * @returns true si x est considéré plus petit que y, false sinon.
 * (On rappelle qu'on travaille avec des files de priorité min)
 */
bool est_plus_petit_par_defaut(type_base x, type_base y);


/**
 * @brief Renvoie une file de priorité vide. \n
 * Par défaut, le champ `est_plus_petit` sera l'adresse de la fonction 
 * `est_plus_petit_par_defaut` écrite ci-dessus.\n
 * **Complexité :** O(1)
 * @returns une file de priorité sans éléments.
 */
FilePriorite file_priorite_vide();


/**
 * @brief Libère la mémoire associée à une file de priorité.
 * On désallouera la liste "valeurs" en plus de la file de priorité elle-même. \n
 * **Complexité :** O(1)
 * @param f la file de priorité qu'on souhaite désallouer.
 */
void liberer_file_priorite(FilePriorite f);


/**
 * @brief Renvoie le nombre d'élements dans la file de priorité. \n
 * **Complexité :** O(1)
 * @param f une file de priorité.
 */
size_t longueur_file_priorite(FilePriorite f);


/**
 * @brief Renvoie la position de l'enfant gauche.\n
 * Attention les index commencent ici à 0, et non pas 1 comparé au cours. \n
 * **Complexité :** O(1)
 * @param pos un index dans le champ `valeurs` d'une file de priorité.
 * @returns l'index de l'enfant qui se situe à gauche de l'élément
 */
size_t position_enfant_gauche(size_t pos);


/**
 * @brief Renvoie la position de l'enfant droit.\n
 * Attention les index commencent ici à 0, et non pas 1 comparé au cours. \n
 * **Complexité :** O(1)
 * @param pos un index dans le champ `valeurs` d'une file de priorité.
 * @returns l'index de l'enfant qui se situe à droite de l'élément
 */
size_t position_enfant_droit(size_t pos);


/**
 * @brief Renvoie la position du parent.\n
 * Attention les index commencent ici à 0, et non pas 1 comparé au cours.
 * Provoque une erreur si jamais l'argument vaut 0. \n
 * **Complexité :** O(1)
 * @param pos un index dans le champ `valeurs` d'une file de priorité.
 * @returns l'index du parent
 */
size_t position_parent(size_t pos);


/**
 * @brief Ajoute un élément dans une file de priorité. \n
 * **Complexité (amortie) :** O(log(n)), où n est le nombre d'éléments.
 * @param f une file de priorité,
 * @param x l'élement à rajouter.
 */
void ajouter_file_priorite(FilePriorite f, type_base x);



/**
 * @brief Renvoie l'élément plus petit d'une file de priorité. \n
 * Provoque une erreur si la file est vide. \n
 * **Complexité :** O(1)
 * @param f une file de priorité.
 * @returns l'élément minimum de f.
 */
type_base minimum(FilePriorite f);
 
/**
 * @brief Supprime et renvoie l'élément le plus petit d'une file de priorité
 * (La file doit être modifiée.) \n
 * Provoque une erreur si la file est vide. \n
 * **Complexité :** O(log(n)), où n est le nombre d'éléments. 
 * @param f une file de priorité.
 * @returns l'élément minimum de f.
 */
type_base extraire_minimum(FilePriorite f);


/**
 * @brief Convertit une liste en une file de priorité min ou max. \n
 * **Complexité :** O(n), où n est la taille de la liste.
 * C'est assez facile de faire une fonction en O(n log(n)), mais
 * toute la subtilité de l'exercice est réussir à écrire un algo linéaire ! \n
 * Indice 1 : Comment feriez-vous pour un tableau de taille 3 ?
 * Et du moment que vous savez faire pour un tableau de taille 3,
 * comment faire pour un tableau de taille 7 ? \n
 * Indice 2 : essayez d'appliquer la technique de 
 * descente que vous avez du utiliser dans la fonction "extraire_minimum"
 * @param l une liste,
 * @param est_file_min un booléen qui vaut `true` si on veut une file min
 * `false`si on veut une file max.
 * @returns une file de priorité **minimum** contenant les mêmes éléments que l
 * si est_file_min est vrai,
 * une file de priorité **maximum** contenant les mêmes éléments que l
 * si est_file_max est vrai.
 */
FilePriorite liste_vers_file_priorite(Liste l, bool est_file_min);



/**
 * @brief Trie une liste (selon l'ordre indiqué par `est_plus_petit_par_defaut`) \n
 * On utilisera pour cela le tri par tas :
 * on commence par transformer la liste en file de priorité,
 * puis on extraira au fur et à mesure l'élément minimal. \n
 * **Complexité :** O(n log(n)), où n est la taille de la liste.
 * @param l une liste.
 */
void tri_par_tas(Liste l);


#endif
