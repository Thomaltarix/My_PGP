##
## EPITECH PROJECT, 2024
## MyPGP
## File description:
## Makefile
##

NAME = my_pgp

MAIN = src/main.py

all: $(NAME)

$(NAME):
	cp $(MAIN) $(NAME)
	chmod +x $(NAME)

clean:
	rm -rf $(NAME)

fclean: clean

re:	fclean all
