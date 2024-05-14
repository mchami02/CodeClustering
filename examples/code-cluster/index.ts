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
import { MouseCoords } from "sigma/types";
import {editor} from 'monaco-editor';
// import loader from '@monaco-editor/loader';

const RED = "#FA4F40";
const BLUE = "#727EE0";

// 1. Load CSV file:
Papa.parse<{ Code_Block: string; Cluster: number; Summary : string }>("./code_clusters_9999.csv", {
  download: true,
  header: true,
  delimiter: ",",
  complete: (results) => {
    const graph: Graph = new Graph();
    const logsDOM = document.getElementById("sigma-logs") as HTMLElement;


    // 2. Build the bipartite graph:
    results.data.forEach((line) => {
      const CodeType = line.Code_Block;
      const IT = line.Summary;
      // const Distance = line.Distance;

      // Create the institution node:
      if (!graph.hasNode(IT)) {
        graph.addNode(IT, {
          nodeType: "Implementation",
          // label: "",
          color: RED,
          size: 10,
          summary : IT
        });
      }

      // Extract subjects list:
      const subject = CodeType;
      // console.log(subject);
      // For each subject, create the node if it does not exist yet:
      graph.addNode(CodeType, { nodeType: "Code", summary: subject, color: BLUE, size: 4 });
      // console.log(Distance);
      graph.addEdge(IT, subject, {size: 1});

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
    // const s = new Sigma(graph, container);
    // s.bind('clickNode', function(e) {
    //   console.log(e.data.node.label)
    // })

    const monaco_editor = editor.create(document.getElementById("container"), {
      value: "print('Hello, world!')",
      language: "python",
      readOnly: true
    });

    // logsDOM.appendChild(document.createElement("div"));
    function logEvent(event: string, item: string | MouseCoords): void {
      const label = graph.getNodeAttribute(item, "summary");
      monaco_editor.setValue(label)
      // div.innerHTML = `<span>${message}</span>`;
      // // logsDOM.appendChild(div);
      // logsDOM.replaceChild(div, logsDOM.firstChild);
      // logsDOM.scrollTo({ top: logsDOM.scrollHeight });
  
    }

    const renderer = new Sigma(graph, container)

    const nodeEvents = [
      "clickNode",
    ] as const;
    
    nodeEvents.forEach((eventType) => renderer.on(eventType, ({ node }) => logEvent(eventType, node)));


  },  
});
