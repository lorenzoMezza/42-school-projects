# Compiler settings
CC = cc
CFLAGS = -Wall -Wextra -Werror

# Source files
SRC = main.c error_handler.c ginevra.c matteo_final.c parse_dict.c utils.c utils2.c utils3.c

# Object files (derived from the source files)
OBJ = $(SRC:.c=.o)

# Output executable
EXEC = ilterzettoperfetto

# Default target (make)
all: $(EXEC)

# Linking the object files into an executable
$(EXEC): $(OBJ)
	$(CC) $(OBJ) -o $(EXEC)

# Compiling each source file into an object file
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up generated files
clean:
	rm -f $(OBJ) $(EXEC)

# Fully clean: remove everything from the build (object files, executable, etc.)
fclean: clean
	rm -f $(EXEC)  # Already done in clean

