#include "rush02.h"
//gcc -Wall -Wextra -Werror main_dict_Test.c parse_dict.c utils.c -o test_dict./test_dict

//MAIN FATTO SOL OPER TESTARE SE LA CONVERISONE DA FILE A **T_DIC E CORETTA 
int	main(void)
{
	t_dict	*dict;
	int		size;
	int		i;

	ft_putstr("=== TEST PARSING DIZIONARIO ===\n\n");
	
	//prova a parsare il file numbers.dict
	ft_putstr("Caricamento file 'numbers.dict'...\n");
	dict = ft_parse_dict("numbers.dict", &size);
	
	if (!dict)
	{
		ft_putstr("ERRORE: mpossibile caricare il dizionario dio bestia!\n");
		ft_putstr("Verifica che il file 'numbers.dict' esista.\n");
		return (1);
	}
	
	ft_putstr(" file caricato con successo!\n\n");
	ft_putstr("Numero di entry valide trovate :vedere bonus: : ");
	// Stampa il numero di entry
	i = size;
	if (i == 0)
		ft_putstr("0");
	else
	{
		char num[20];
		int j = 0;
		while (i > 0)
		{
			num[j++] = (i % 10) + '0';
			i /= 10;
		}
		while (j > 0)
			write(1, &num[--j], 1);
	}
	ft_putstr("\n\n");
	
	ft_putstr("=== CONTENUTO DEL FOTTUTO DIZIONARIO ===\n\n");
	

	i = 0;
	while (i < size)
	{
		ft_putstr("Entry [");
		
		if (i < 10)
		{
			char c = i + '0';
			write(1, &c, 1);
		}
		else
		{
			char num[20];
			int temp = i;
			int j = 0;
			while (temp > 0)
			{
				num[j++] = (temp % 10) + '0';
				temp /= 10;
			}
			while (j > 0)
				write(1, &num[--j], 1);
		}
		ft_putstr("]\n");
		ft_putstr("  Key   : \"");
		ft_putstr(dict[i].key);
		ft_putstr("\"\n");
		ft_putstr("  Value : \"");
		ft_putstr(dict[i].value);
		ft_putstr("\"\n\n");
		i++;
	}
	

	ft_putstr("Il dizionario è stato parsato correttamente SE SIAMO QUI!\n");
	
	// Libera la memoria
	//NON DOVREBBE DALLIRE CIO 
	ft_free_dict(dict, size);
	
	return (0);
}
