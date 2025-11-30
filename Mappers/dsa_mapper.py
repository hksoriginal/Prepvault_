from Instructions.DSA.BST import BST_
from Instructions.DSA.LinkedList import ll_ds
from Instructions.DSA.dp import dp
from Instructions.DSA.stack import stack
from Instructions.DSA.queue import queue


DSA_MAPPER = {
    "Stack": [
        stack,
        "https://leetcode.com/problem-list/stack/", "https://www.youtube.com/results?search_query=stack+in+python"
    ],
    "Queue": [
        queue,
        "https://leetcode.com/problem-list/queue/", "https://www.youtube.com/results?search_query=queue+in+python"
    ],
    "Linked List": [
        ll_ds,
        "https://leetcode.com/problem-list/linked-list/", "https://www.youtube.com/results?search_query=linked+list+in+python"
    ],
    "Binary Search Tree": [
        BST_,
        "https://leetcode.com/problem-list/binary-search-tree/", "https://www.youtube.com/results?search_query=BST+in+Python"
    ],

    "Dynamic Programming": [
        dp,
        "https://leetcode.com/problem-list/dynamic-programming/", "https://www.youtube.com/results?search_query=Dynamic+programming+in+python"
    ],

}
