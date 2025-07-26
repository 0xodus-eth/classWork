#include <iostream>
#include <vector>
#include <climits>
#include <queue>
#include <iomanip>
using namespace std;

class Graph
{
private:
    int V;                         // Number of vertices
    vector<vector<int>> adjMatrix; // Adjacency matrix

public:
    // Constructor
    Graph(int vertices)
    {
        V = vertices;
        adjMatrix.resize(V, vector<int>(V, 0));
    }

    // Add edge to the graph
    void addEdge(int u, int v, int weight)
    {
        adjMatrix[u][v] = weight;
        // For undirected graph, uncomment the next line
        // adjMatrix[v][u] = weight;
    }

    // Utility function to find vertex with minimum distance
    int minDistance(vector<int> &dist, vector<bool> &visited)
    {
        int min = INT_MAX, min_index = -1;

        for (int v = 0; v < V; v++)
        {
            if (!visited[v] && dist[v] <= min)
            {
                min = dist[v];
                min_index = v;
            }
        }
        return min_index;
    }

    // Print the shortest path from source to target
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

    // Print solution
    void printSolution(vector<int> &dist, vector<int> &parent, int src)
    {
        cout << "\n=== DIJKSTRA'S ALGORITHM RESULTS ===\n";
        cout << "Source Vertex: " << src << "\n\n";
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
    }

    // Dijkstra's algorithm implementation using adjacency matrix
    void dijkstra(int src)
    {
        vector<int> dist(V, INT_MAX);   // Distance array
        vector<bool> visited(V, false); // Visited array
        vector<int> parent(V, -1);      // Parent array to store path

        // Distance from source to itself is 0
        dist[src] = 0;

        // Find shortest path for all vertices
        for (int count = 0; count < V - 1; count++)
        {
            // Pick minimum distance vertex from unvisited vertices
            int u = minDistance(dist, visited);

            if (u == -1)
                break; // No more reachable vertices

            // Mark the picked vertex as visited
            visited[u] = true;

            // Update distance values of adjacent vertices
            for (int v = 0; v < V; v++)
            {
                // Update dist[v] if:
                // 1. Not visited
                // 2. There is an edge from u to v
                // 3. Total weight from src to v through u is smaller than current dist[v]
                if (!visited[v] && adjMatrix[u][v] != 0 &&
                    dist[u] != INT_MAX && dist[u] + adjMatrix[u][v] < dist[v])
                {
                    dist[v] = dist[u] + adjMatrix[u][v];
                    parent[v] = u;
                }
            }
        }

        // Print the solution
        printSolution(dist, parent, src);
    }

    // Display the adjacency matrix
    void displayGraph()
    {
        cout << "\n=== ADJACENCY MATRIX ===\n";
        cout << "   ";
        for (int i = 0; i < V; i++)
        {
            cout << setw(4) << i;
        }
        cout << "\n";

        for (int i = 0; i < V; i++)
        {
            cout << i << ": ";
            for (int j = 0; j < V; j++)
            {
                if (adjMatrix[i][j] == 0)
                {
                    cout << setw(4) << "∞";
                }
                else
                {
                    cout << setw(4) << adjMatrix[i][j];
                }
            }
            cout << "\n";
        }
    }
};

// Alternative implementation using adjacency list and priority queue
class GraphList
{
private:
    int V;
    vector<vector<pair<int, int>>> adjList; // pair<vertex, weight>

public:
    GraphList(int vertices)
    {
        V = vertices;
        adjList.resize(V);
    }

    void addEdge(int u, int v, int weight)
    {
        adjList[u].push_back({v, weight});
        // For undirected graph, uncomment the next line
        // adjList[v].push_back({u, weight});
    }

    void dijkstraOptimized(int src)
    {
        // Priority queue to store {distance, vertex}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        vector<int> dist(V, INT_MAX);
        vector<int> parent(V, -1);

        dist[src] = 0;
        pq.push({0, src});

        while (!pq.empty())
        {
            int u = pq.top().second;
            pq.pop();

            // Traverse all adjacent vertices
            for (auto &edge : adjList[u])
            {
                int v = edge.first;
                int weight = edge.second;

                // If shorter path found
                if (dist[u] + weight < dist[v])
                {
                    dist[v] = dist[u] + weight;
                    parent[v] = u;
                    pq.push({dist[v], v});
                }
            }
        }

        // Print results
        cout << "\n=== OPTIMIZED DIJKSTRA (Priority Queue) ===\n";
        cout << "Source Vertex: " << src << "\n\n";
        cout << "Vertex\tDistance\n";
        cout << "------\t--------\n";

        for (int i = 0; i < V; i++)
        {
            cout << i << "\t";
            if (dist[i] == INT_MAX)
            {
                cout << "INF\n";
            }
            else
            {
                cout << dist[i] << "\n";
            }
        }
    }
};

int main()
{
    int choice, vertices, edges, src;

    cout << "=== DIJKSTRA'S SHORTEST PATH ALGORITHM ===\n\n";
    cout << "Choose implementation:\n";
    cout << "1. Adjacency Matrix (Basic)\n";
    cout << "2. Adjacency List with Priority Queue (Optimized)\n";
    cout << "3. Predefined Example\n";
    cout << "Enter choice (1-3): ";
    cin >> choice;

    if (choice == 3)
    {
        // Predefined example
        cout << "\n=== PREDEFINED EXAMPLE ===\n";
        Graph g(6);

        // Add edges (u, v, weight)
        g.addEdge(0, 1, 4);
        g.addEdge(0, 2, 2);
        g.addEdge(1, 2, 1);
        g.addEdge(1, 3, 5);
        g.addEdge(2, 3, 8);
        g.addEdge(2, 4, 10);
        g.addEdge(3, 4, 2);
        g.addEdge(3, 5, 6);
        g.addEdge(4, 5, 3);

        g.displayGraph();
        g.dijkstra(0); // Source vertex 0

        // Also show optimized version
        GraphList gl(6);
        gl.addEdge(0, 1, 4);
        gl.addEdge(0, 2, 2);
        gl.addEdge(1, 2, 1);
        gl.addEdge(1, 3, 5);
        gl.addEdge(2, 3, 8);
        gl.addEdge(2, 4, 10);
        gl.addEdge(3, 4, 2);
        gl.addEdge(3, 5, 6);
        gl.addEdge(4, 5, 3);

        gl.dijkstraOptimized(0);
    }
    else
    {
        cout << "Enter number of vertices: ";
        cin >> vertices;

        cout << "Enter number of edges: ";
        cin >> edges;

        if (choice == 1)
        {
            Graph g(vertices);

            cout << "Enter edges (source destination weight):\n";
            for (int i = 0; i < edges; i++)
            {
                int u, v, w;
                cin >> u >> v >> w;
                g.addEdge(u, v, w);
            }

            cout << "Enter source vertex: ";
            cin >> src;

            g.displayGraph();
            g.dijkstra(src);
        }
        else if (choice == 2)
        {
            GraphList g(vertices);

            cout << "Enter edges (source destination weight):\n";
            for (int i = 0; i < edges; i++)
            {
                int u, v, w;
                cin >> u >> v >> w;
                g.addEdge(u, v, w);
            }

            cout << "Enter source vertex: ";
            cin >> src;

            g.dijkstraOptimized(src);
        }
    }

    return 0;
}
