#include "lists.h"
/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome
 * @head: header of the singly linked list
 * Return: 0 if is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	size_t i = 0, j = 0, l = 0, k = 0;
	listint_t *kola;

	if (head == NULL || *head == NULL)
		return (1);
	kola = *head;
	for (i = 0; kola->next; i++)
		kola = kola->next;
	j = i / 2;
	l = i - 2;
	for (i = 0; i < j; i++)
	{
		if ((*head)->n == kola->n)
		{
			*head = (*head)->next;
			kola = *head;
			for (k = 0; k < l; k++)
				kola = kola->next;
			if ((*head)->n == kola->n)
				l -= 2;
			else
				return (0);
		}
		else
			return (0);
	}
	return (1);
}
