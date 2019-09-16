#include "lists.h"
/**
 * check_cycle - function for check if a singly linked list has a cycle in it
 * @list: header for the single linked list
 * Return: 0 if there is no cycly, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *w;

	if (list == NULL || list->next == NULL)
		return (0);

	w = list;

	while (list)
	{
		if (w == list->next)
			return (1);
		list = list->next;
	}
	return (0);
}
