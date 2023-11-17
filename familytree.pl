male(shankar).
male(ulash).
male(satish).
male(saurabh).
male(pranav).
female(umabai).
female(swati).
female(mrunal).
female(sadhana).

parent(shankar, umabai).
parent(shankar, satish).
parent(shankar, ulash).
parent(umabai, swati).
parent(umabai, sadhana).
parent(umabai, saurabh).
parent(ulash, mrunal).
parent(ulash, pranav).

sister(X, Y):- parent(Z, X), parent(Z, Y), female(X), X\==Y.
brother(X, Y):- parent(Z, X), parent(Z, Y), male(X), X\==Y.

uncle(X, Z):- brother(X, Y), parent(Y, Z).
aunt(X, Z):- sister(X, Y), parent(Y, Z).
grandparent(X, Y):- parent(X, Z), parent(Z, Y).

cousin(X, Y):- grandparent(Z, X), grandparent(Z, Y) , X\==Y.