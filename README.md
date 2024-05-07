# Cluster Visualization using Sigma and Monaco Editor

## Overview

### Architecture

We use the library SigmaJS to render the graph visualization interface. With it, we can easily visualize the clusters, move around the different groups, and see the labels of the code snippets.

We use monaco-editor to render the code editor interface located at the top of the screen. By clicking on one of the nodes, the associated code appears on the code editor, which is in read-only mode.

## Installation

Use npm to install all the necessary packages from the main directory.

```bash
npm install
```

### Build

To simply run the website with the graph and the code editor, go to the `examples` folder and run :

```bash
npm start --example=code-cluster
```

The website will be hosted on [http://localhost:3000]