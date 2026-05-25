# Get Next Line

*This project has been created as part of the 42 curriculum by <lmezzaba>.*

---

## Description

Il progetto **Get Next Line** consiste nell’implementare una funzione in C che permette di leggere un file descriptor una riga alla volta.

L’obiettivo è costruire una funzione capace di restituire, ad ogni chiamata, la prossima riga disponibile da un file, dallo standard input o da qualsiasi file descriptor valido.

La funzione deve:
- gestire correttamente la memoria dinamica
- mantenere lo stato tra chiamate successive
- funzionare con qualsiasi valore di `BUFFER_SIZE`

---

## Algorithm Overview

L’implementazione si basa su una logica di accumulo e parsing progressivo dei dati letti.

### Static stash
Viene utilizzata una variabile statica (`static char *stash`) per conservare i dati letti ma non ancora restituiti.

### Lettura a blocchi
La funzione utilizza `read()` con dimensione `BUFFER_SIZE` per leggere il file a blocchi.

### Concatenazione
I dati letti vengono aggiunti allo stash fino a quando non viene trovata una `\n`.

### Estrazione della riga
Quando viene trovata una newline:
- viene estratta la riga completa
- il resto dei dati rimane nello stash per la prossima chiamata

### Gestione EOF
Se non ci sono più dati da leggere, viene restituito l’ultimo contenuto rimasto nello stash.

---

## Instructions

### Compilation

Per compilare il progetto:

```bash
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 *.c