#include "lists.h"

/**
 * dlistint_len - func that print all element
 * @h: pointer of the list
 * Return: always nodes
 */
size_t dlistint_len(const dlistint_t *h)
{
	int x;

	x = 0;

	if (h == NULL)
		return (x);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		x++;
		h = h->next;
	}

	return (x);
}
