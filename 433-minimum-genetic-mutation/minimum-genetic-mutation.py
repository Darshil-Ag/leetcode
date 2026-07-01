from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        bank = set(bank)

        if endGene not in bank:
            return -1

        q = deque([(startGene, 0)])
        visited = set([startGene])
        genes = ['A', 'C', 'G', 'T']

        while q:
            gene, steps = q.popleft()

            if gene == endGene:
                return steps

            for i in range(8):
                for ch in genes:
                    if ch != gene[i]:
                        new_gene = gene[:i] + ch + gene[i + 1:]

                        if new_gene in bank and new_gene not in visited:
                            visited.add(new_gene)
                            q.append((new_gene, steps + 1))

        return -1