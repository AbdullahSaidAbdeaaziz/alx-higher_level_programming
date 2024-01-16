#include "lists.h"

/**
 * insert_node - insert a node into sorted
 * single liked list
 * @head: first node in list
 * @number: node that will be inserted
 * Return: node that have been inserted, NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current;

	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;

	if (!*head || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
	} else
	{
		current = *head;
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);
}
