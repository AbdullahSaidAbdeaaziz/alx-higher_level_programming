#include "lists.h"

/**
 * compareLists - compares two linked lists.
 * @head1: A pointer to the head of the first linked list.
 * @head2: A pointer to the head of the second linked list.
 * Return: It returns 1 if the linked lists are identical,
 * otherwise it returns 0.
 */

int compareLists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}

/**
 * reverse - reverses a singly linked list.
 * @head_ref: A pointer to the head of the linked list.
 * It modifies the list in place
 * Return: None
 */
void reverse(listint_t **head_ref)
{
	listint_t *prev = NULL;
	listint_t *current = *head_ref;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_ref = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: A pointer to the head of the linked list
 * Return: It returns 1 if the linked list is a palindrome,
 * otherwise it returns 0.
 * An empty list is considered a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = *head,
	*second_half, *middle = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
	while (fast && fast->next)
	{
	fast = fast->next->next;
	prev = slow;
	slow = slow->next;
	}

	if (fast != NULL)
	{
	middle = slow;
	slow = slow->next;
	}

	second_half = slow;
	prev->next = NULL;
	reverse(&second_half);
	res = compareLists(*head, second_half);

	reverse(&second_half);

	if (middle != NULL)
	{
	prev->next = middle;
	middle->next = second_half;
	}
	else
	prev->next = second_half;
	}
	return (res);
}
