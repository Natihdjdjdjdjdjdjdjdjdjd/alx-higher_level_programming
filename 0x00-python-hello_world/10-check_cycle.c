#include "lists.h"
/**
 * check_cycle -  function in C that checks if a singly linked list
 * @list: the  link tha we check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *decrease = list;
	listint_t *increase = list;

	if (!list)
		return (0);

	while (decrease && increase && increase->next)
	{
		decrease = decrease->next;
		increase = increase->next->next;
		if (decrease == increase)
			return (1);
	}
	return (0);
}
