#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head node
 * Return: 0, if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	/**
	 * get the length of the list
	 * if the length is even:
	 * - put a pointer to half
	 * else:
	 * - put a pointer to half + 1
	 * from pointer, reverse the list
	 * from the reversed list, set the head
	 * compare the original list(first half) and the reversed
	 * loop only half-1 times
	 * if compare is successful, return 1
	 * else: return -1
	 */
	listint_t *ptr, *hd;
	int half, i, len = 0;

	if (head == NULL || *head == NULL)
		return (0);
	ptr = *head;
	while (ptr)
	{
		len++;
		ptr = ptr->next;
	}
	half = len / 2;
	ptr = *head;
	for (i = 0; i < half; i++)
		ptr = ptr->next;

	/* printf("Middle node is: %d\n", ptr->n); */
	hd = reverse_list(ptr);
	return (compare(*head, hd));
}

/**
 * reverse_list - reverses the linked list
 * @ptr: pointer to the first node of the list
 * Return: a pointer to the head of the reversed list
 */
listint_t *reverse_list(listint_t *ptr)
{
	listint_t *cur, *head;

	cur = ptr->next;
	ptr->next = NULL;
	while (cur)
	{
		head = cur;
		cur = head->next;
		head->next = ptr;
		ptr = head;
	}
	return (head);
}

/**
 * compare - compares the two lists
 * @head: pointer to the first node of the first list
 * @hd: pointer to the first node of the second list.
 * Return: 0, if it is not a palindrome, 1 if it is
 */
int compare(listint_t *head, listint_t *hd)
{
	while (head && hd)
	{
		if (head->n != hd->n)
			return (0);
		head = head->next;
		hd = hd->next;
	}
	return (1);
}
