/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ginevra.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gicinzio <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/31 14:57:13 by gicinzio          #+#    #+#             */
/*   Updated: 2026/01/31 19:06:28 by gicinzio         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
int	ft_strlen(char *str)
{
	int	i;
	i = 0;
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}
void	check_3(char *str)
{
	int	j;

	j = ft_strlen(str);
	if (j == 3)
	{
		if(str[0] == '0' || str[1] != '0' && str[2] != '0')
		{
			//passa alla funzione delle decine
			check_2(str + 1);
		}
		if(str[0] >= '1' && str[0] <= '9')
		{
			//print dict n
			write(1, " ", 1);
			//print ditc hundred
			if(str[1] == '0' && str[2] == '0')
			{
				return;
				//se ho stampato le centinia e str[1 e 2] sono zero
				//allora non ci sono decine.
			}
		}
	}
}
void	check_2(char *str)
{
	int	j;
	
	j = strlen(str);

	if(j == 2)
	{
		if (str[0] == '0' && str[1] != '0')
		{
			//siamo alle unita;
			//print ditc unita'
		}
		if((str[0] >= '1' && str[0] <= '9') && str[1] == '0')
		{
			//siamo alle decine tipo 10, 20 etc..
			//quindi niente (space)
		}
		if((str[0] >= '1' && str[0] <= '9') && (str[1] >= '1' && str[1] <= '9'))
		{
			//siamo alle decine 10, 20 etc.. e alle unita, quindi...
			//print ditch str[0] ex twenty..
			write(1, " ", 1);
			//print ditch n str[1] ex four..
		}
	}
}
int	main()
{
	char str[] = "123";
	check_3(str);
	return 0;
}	
