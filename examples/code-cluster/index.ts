/**
 * This example shows how to use graphology and sigma to interpret a dataset and
 * to transform it to a mappable graph dataset, without going through any other
 * intermediate step.
 *
 * To do this, we start from a dataset from "The Cartography of Political
 * Science in France" extracted from:
 * https://cartosciencepolitique.sciencespo.fr/#/en
 *
 * The CSV contains one line per institution, with an interesting subject_terms
 * column. We will here transform this dataset to a institution/subject
 * bipartite network map.
 */

import Sigma from "sigma";
import Papa from "papaparse";
import Graph from "graphology";
import circular from "graphology-layout/circular";
import forceAtlas2 from "graphology-layout-forceatlas2";
import { cropToLargestConnectedComponent } from "graphology-components";

const RED = "#FA4F40";
const BLUE = "#727EE0";

// 1. Load CSV file:
Papa.parse<{ CodeID: string; IT: number; Distance: number }>("./clustering_data.csv", {
  download: true,
  header: true,
  delimiter: ",",
  complete: (results) => {
    const graph: Graph = new Graph();

    // 2. Build the bipartite graph:
    results.data.forEach((line) => {
      const CodeType = line.CodeID;
      const IT = line.IT;
      const Distance = line.Distance;

      // Create the institution node:
      if (!graph.hasNode(IT)) {
        graph.addNode(IT, {
          nodeType: "Implementation",
          label: IT,
          color: RED,
          size: 10
        });
      }

      // Extract subjects list:
      const subject = CodeType;
      console.log(subject);
      // For each subject, create the node if it does not exist yet:
      graph.addNode(CodeType, { nodeType: "Code", label: CodeType, color: BLUE, size: 4 });
      // console.log(Distance);
      graph.addEdge(IT, subject, {size: Distance});

    });

    // 4. Add colors to the nodes, based on node types:
    // const COLORS: Record<string, string> = { IT: "#FA5A3D", CodeType: "#5A75DB" };
    // graph.forEachNode((node, attributes) =>
    //   graph.setNodeAttribute(node, "color", COLORS[attributes.nodeType as string]),
    // );

    // 5. Use degrees for node sizes:
    // const degrees = graph.nodes().map((node) => graph.degree(node));
    // const minDegree = Math.min(...degrees);
    // const maxDegree = Math.max(...degrees);
    // const minSize = 2,
    //   maxSize = 15;
    // graph.forEachNode((node) => {
    //   const degree = graph.degree(node);
    //   graph.setNodeAttribute(
    //     node,
    //     "size",
    //     minSize + ((degree - minDegree) / (maxDegree - minDegree)) * (maxSize - minSize),
    //   );
    // });

    // 6. Position nodes on a circle, then run Force Atlas 2 for a while to get
    //    proper graph layout:
    circular.assign(graph);
    const settings = forceAtlas2.inferSettings(graph);
    forceAtlas2.assign(graph, { settings, iterations: 100 });

    // 7. Hide the loader from the DOM:
    const loader = document.getElementById("loader") as HTMLElement;
    loader.style.display = "none";

    // 8. Finally, draw the graph using sigma:
    const container = document.getElementById("sigma-container") as HTMLElement;
    new Sigma(graph, container);
  },
});
