#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the first node
 * @number: the node value
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *curr, *node;

	if (head == NULL)
		return (NULL);

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}

	prev = *head;
	curr = prev->next;

	while (curr)
	{
		if (curr->n >= number && prev->n <= number)
		{
			prev->next = node;
			node->next = curr;
			break;
		}
		prev = curr;
		curr = curr->next;
	}
	if (curr == NULL)
	{
		if (prev->n > number)
		{
			node->next = prev;
			*head = node;
		}
		else
			prev->next = node;
	}
	return (node);
}
