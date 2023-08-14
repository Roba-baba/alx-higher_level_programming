#include "lists.h"

/**
 * palindrom -  recursive or not a palindrom.
 * @head: the head list.
 *
 * Return: 0 if not a palindrome else 1
 *
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - function to test if palindrome.
 * @head: the head list
 *
 * @end: the end of the list.
 */
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
