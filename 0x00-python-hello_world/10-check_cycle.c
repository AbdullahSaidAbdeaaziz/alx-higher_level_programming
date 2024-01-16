#include "lists.h"

/**
 * check_cycle - check cycle in single
 * linked list in efficient way
 * @list: single linked list
 * Return: 1 if cycle, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;
	if (!list)
	{
		return (0);
	}
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
