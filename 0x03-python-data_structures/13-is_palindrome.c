#include "lists.h"


/**
 * reverse_list - reverse single linked list
 * @head: first node
 * Return: first node in reverse list
*/
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *cur = *head;
	listint_t *next = NULL;

	while (cur != NULL)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	*head = prev;
	return *head;

}

/**
 * is_palindrome - checks if single linked
 * list is a palindrome
 * @head: cur node in single linked list
 * Return: 1 if palindrome, 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	listint_t *last, *cur;

	if (!head || !*head || !(*head)->next)
	{
		return (1);
	}

	last = reverse_list(head);
	cur = *head;
	while (cur != NULL && last != NULL)
	{
		if (cur->n != last->n)
		{
			return (0);
		}
		last = last->next;
		cur = cur->next;
	}
	return (1);
}
