#include <stdlib.h>

#define BUFFER_SIZE 42
#define MAX 100

char	*get_next_line(int fd)
{
    if (fd < 0 || fd >= MAX || BUFFER_SIZE <= 0)
	    return (NULL);
	char		*line;
	char		*tempLine;
	char		*newline;
	static char	*stash[MAX];
	size_t		bytesRead;
	int			i;
	int			j;

	line = NULL;

	while (1)
	{
		if (!stash[fd])
		{
			stash[fd] = malloc(sizeof(char) * (BUFFER_SIZE + 1));
			if (!stash[fd])
				return (NULL);

			bytesRead = read(fd, stash[fd], BUFFER_SIZE);

			if (bytesRead <= 0)
			{
				free(stash[fd]);
				stash[fd] = NULL;
				return (line);
			}

			stash[fd][bytesRead] = '\0';
		}

		i = 0;
		while (stash[fd][i] && stash[fd][i] != '\n')
			i++;

		tempLine = malloc(sizeof(char) * (i + 2));
		if (!tempLine)
			return (NULL);

		j = 0;
		while (j < i)
		{
			tempLine[j] = stash[fd][j];
			j++;
		}

		if (stash[fd][i] == '\n')
		{
			tempLine[j] = '\n';
			j++;
		}

		tempLine[j] = '\0';

		if (!line)
		{
			line = tempLine;
		}
		else
		{
			newline = ft_strjoin(line, tempLine);
			free(line);
			free(tempLine);
			line = newline;
		}

		if (stash[fd][i] == '\n')
		{
			j = 0;
			i++;

			while (stash[fd][i])
				stash[fd][j++] = stash[fd][i++];

			stash[fd][j] = '\0';

			return (line);
		}
		else
		{
			free(stash[fd]);
			stash[fd] = NULL;
		}
	}

	return (NULL);
}

