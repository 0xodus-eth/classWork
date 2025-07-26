#include <iostream>
#include <vector>
#include <climits>
#include <chrono>
#include <iomanip>
using namespace std;
using namespace std::chrono;

// Min-Heap implementation for Dijkstra's algorithm
class MinHeap
{
private:
    vector<pair<int, int>> heap; // pair<distance, vertex>
    vector<int> pos;             // position of vertex in heap
    int size;

    void swap(int i, int j)
    {
        pos[heap[i].second] = j;
        pos[heap[j].second] = i;
        std::swap(heap[i], heap[j]);
    }

    void minHeapify(int idx)
    {
        int smallest = idx;
        int left = 2 * idx + 1;
        int right = 2 * idx + 2;

        if (left < size && heap[left].first < heap[smallest].first)
            smallest = left;

        if (right < size && heap[right].first < heap[smallest].first)
            smallest = right;

        if (smallest != idx)
        {
            swap(idx, smallest);
            minHeapify(smallest);
        }
    }

public:
    MinHeap(int V)
    {
        heap.resize(V);
        pos.resize(V);
        size = 0;
    }

    bool isEmpty()
    {
        return size == 0;
    }

    pair<int, int> extractMin()
    {
        if (isEmpty())
            return {-1, -1};

        pair<int, int> root = heap[0];
        pair<int, int> lastNode = heap[size - 1];

        heap[0] = lastNode;
        pos[lastNode.second] = 0;
        pos[root.second] = -1; // Mark as extracted

        size--;
        minHeapify(0);

        return root;
    }

    void decreaseKey(int v, int dist)
    {
        int i = pos[v];
        heap[i].first = dist;

        while (i && heap[i].first < heap[(i - 1) / 2].first)
        {
            swap(i, (i - 1) / 2);
            i = (i - 1) / 2;
        }
    }

    bool isInMinHeap(int v)
    {
        return pos[v] != -1 && pos[v] < size;
    }

    void insert(int v, int dist)
    {
        heap[size] = {dist, v};
        pos[v] = size;
        size++;

        int i = size - 1;
        while (i && heap[i].first < heap[(i - 1) / 2].first)
        {
            swap(i, (i - 1) / 2);
            i = (i - 1) / 2;
        }
    }
};

class GraphMinHeap
{
private:
    int V;
    vector<vector<pair<int, int>>> adjList; // pair<vertex, weight>

public:
    GraphMinHeap(int vertices)
    {
        V = vertices;
        adjList.resize(V);
    }

    void addEdge(int u, int v, int weight)
    {
        adjList[u].push_back({v, weight});
    }

    void printPath(vector<int> &parent, int target)
    {
        if (parent[target] == -1)
        {
            cout << target << " ";
            return;
        }
        printPath(parent, parent[target]);
        cout << target << " ";
    }

    // Dijkstra's algorithm using custom min-heap
    microseconds dijkstraMinHeap(int src)
    {
        auto start_time = high_resolution_clock::now();

        vector<int> dist(V, INT_MAX);
        vector<int> parent(V, -1);
        MinHeap minHeap(V);

        // Initialize distances and add all vertices to min heap
        for (int v = 0; v < V; v++)
        {
            if (v == src)
            {
                dist[v] = 0;
                minHeap.insert(v, 0);
            }
            else
            {
                minHeap.insert(v, INT_MAX);
            }
        }

        while (!minHeap.isEmpty())
        {
            pair<int, int> minVertex = minHeap.extractMin();
            int u = minVertex.second;

            // Traverse all adjacent vertices of u
            for (auto &edge : adjList[u])
            {
                int v = edge.first;
                int weight = edge.second;

                // If v is still in min heap and distance through u is shorter
                if (minHeap.isInMinHeap(v) && dist[u] != INT_MAX &&
                    dist[u] + weight < dist[v])
                {
                    dist[v] = dist[u] + weight;
                    parent[v] = u;
                    minHeap.decreaseKey(v, dist[v]);
                }
            }
        }

        auto end_time = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(end_time - start_time);

        // Print results
        cout << "\n=== DIJKSTRA WITH CUSTOM MIN-HEAP ===\n";
        cout << "Source Vertex: " << src << "\n";
        cout << "Execution Time: " << duration.count() << " microseconds\n\n";
        cout << "Vertex\tDistance\tPath\n";
        cout << "------\t--------\t----\n";

        for (int i = 0; i < V; i++)
        {
            if (i != src)
            {
                cout << src << " -> " << i << "\t";
                if (dist[i] == INT_MAX)
                {
                    cout << "INF\t\tNo path\n";
                }
                else
                {
                    cout << dist[i] << "\t\t";
                    printPath(parent, i);
                    cout << "\n";
                }
            }
        }

        return duration;
    }

    // Standard implementation for comparison
    microseconds dijkstraStandard(int src)
    {
        auto start_time = high_resolution_clock::now();

        vector<int> dist(V, INT_MAX);
        vector<bool> visited(V, false);
        vector<int> parent(V, -1);

        dist[src] = 0;

        for (int count = 0; count < V - 1; count++)
        {
            int u = -1;
            for (int v = 0; v < V; v++)
            {
                if (!visited[v] && (u == -1 || dist[v] < dist[u]))
                    u = v;
            }

            if (u == -1 || dist[u] == INT_MAX)
                break;

            visited[u] = true;

            for (auto &edge : adjList[u])
            {
                int v = edge.first;
                int weight = edge.second;

                if (!visited[v] && dist[u] + weight < dist[v])
                {
                    dist[v] = dist[u] + weight;
                    parent[v] = u;
                }
            }
        }

        auto end_time = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(end_time - start_time);

        cout << "\n=== DIJKSTRA STANDARD IMPLEMENTATION ===\n";
        cout << "Source Vertex: " << src << "\n";
        cout << "Execution Time: " << duration.count() << " microseconds\n\n";
        cout << "Vertex\tDistance\tPath\n";
        cout << "------\t--------\t----\n";

        for (int i = 0; i < V; i++)
        {
            if (i != src)
            {
                cout << src << " -> " << i << "\t";
                if (dist[i] == INT_MAX)
                {
                    cout << "INF\t\tNo path\n";
                }
                else
                {
                    cout << dist[i] << "\t\t";
                    printPath(parent, i);
                    cout << "\n";
                }
            }
        }

        return duration;
    }

    void displayGraph()
    {
        cout << "\n=== ADJACENCY LIST REPRESENTATION ===\n";
        for (int i = 0; i < V; i++)
        {
            cout << "Vertex " << i << ": ";
            for (auto &edge : adjList[i])
            {
                cout << "(" << edge.first << "," << edge.second << ") ";
            }
            cout << "\n";
        }
    }
};

// Function to create test graphs
GraphMinHeap createTestGraph1()
{
    // Dense graph - 6 vertices, many edges
    GraphMinHeap g(6);
    g.addEdge(0, 1, 4);
    g.addEdge(0, 2, 2);
    g.addEdge(1, 2, 1);
    g.addEdge(1, 3, 5);
    g.addEdge(2, 3, 8);
    g.addEdge(2, 4, 10);
    g.addEdge(3, 4, 2);
    g.addEdge(3, 5, 6);
    g.addEdge(4, 5, 3);
    g.addEdge(1, 4, 7);
    g.addEdge(0, 5, 15);
    return g;
}

GraphMinHeap createTestGraph2()
{
    // Larger sparse graph - 10 vertices, fewer edges
    GraphMinHeap g(10);
    g.addEdge(0, 1, 10);
    g.addEdge(0, 2, 6);
    g.addEdge(0, 3, 5);
    g.addEdge(1, 3, 15);
    g.addEdge(2, 3, 4);
    g.addEdge(3, 4, 9);
    g.addEdge(3, 5, 13);
    g.addEdge(4, 6, 11);
    g.addEdge(5, 6, 1);
    g.addEdge(5, 7, 14);
    g.addEdge(6, 7, 3);
    g.addEdge(7, 8, 2);
    g.addEdge(8, 9, 6);
    g.addEdge(6, 9, 8);
    return g;
}

int main()
{
    cout << "========================================\n";
    cout << "DIJKSTRA'S ALGORITHM PERFORMANCE COMPARISON\n";
    cout << "========================================\n\n";

    // Test Graph 1: Dense Graph
    cout << "##########################################\n";
    cout << "TEST GRAPH 1: DENSE GRAPH (6 vertices, 11 edges)\n";
    cout << "##########################################\n";

    GraphMinHeap g1 = createTestGraph1();
    g1.displayGraph();

    cout << "\n--- Running Standard Dijkstra ---\n";
    auto time1_standard = g1.dijkstraStandard(0);

    cout << "\n--- Running Min-Heap Dijkstra ---\n";
    auto time1_minheap = g1.dijkstraMinHeap(0);

    cout << "\n=== PERFORMANCE COMPARISON (Graph 1) ===\n";
    cout << "Standard Implementation: " << time1_standard.count() << " microseconds\n";
    cout << "Min-Heap Implementation: " << time1_minheap.count() << " microseconds\n";
    cout << "Speedup: " << fixed << setprecision(2)
         << (double)time1_standard.count() / time1_minheap.count() << "x\n\n";

    // Test Graph 2: Sparse Graph
    cout << "##########################################\n";
    cout << "TEST GRAPH 2: SPARSE GRAPH (10 vertices, 14 edges)\n";
    cout << "##########################################\n";

    GraphMinHeap g2 = createTestGraph2();
    g2.displayGraph();

    cout << "\n--- Running Standard Dijkstra ---\n";
    auto time2_standard = g2.dijkstraStandard(0);

    cout << "\n--- Running Min-Heap Dijkstra ---\n";
    auto time2_minheap = g2.dijkstraMinHeap(0);

    cout << "\n=== PERFORMANCE COMPARISON (Graph 2) ===\n";
    cout << "Standard Implementation: " << time2_standard.count() << " microseconds\n";
    cout << "Min-Heap Implementation: " << time2_minheap.count() << " microseconds\n";
    cout << "Speedup: " << fixed << setprecision(2)
         << (double)time2_standard.count() / time2_minheap.count() << "x\n\n";

    // Overall Summary
    cout << "==========================================\n";
    cout << "OVERALL PERFORMANCE SUMMARY\n";
    cout << "==========================================\n";
    cout << "Graph 1 (Dense):\n";
    cout << "  Standard: " << time1_standard.count() << " μs\n";
    cout << "  Min-Heap: " << time1_minheap.count() << " μs\n";
    cout << "  Improvement: " << fixed << setprecision(1)
         << ((double)(time1_standard.count() - time1_minheap.count()) / time1_standard.count()) * 100 << "%\n\n";

    cout << "Graph 2 (Sparse):\n";
    cout << "  Standard: " << time2_standard.count() << " μs\n";
    cout << "  Min-Heap: " << time2_minheap.count() << " μs\n";
    cout << "  Improvement: " << fixed << setprecision(1)
         << ((double)(time2_standard.count() - time2_minheap.count()) / time2_standard.count()) * 100 << "%\n\n";

    cout << "Time Complexity Analysis:\n";
    cout << "  Standard Implementation: O(V²)\n";
    cout << "  Min-Heap Implementation: O((V + E) log V)\n";
    cout << "  Min-heap is more efficient for sparse graphs!\n";

    return 0;
}
