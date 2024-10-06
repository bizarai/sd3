document.addEventListener('DOMContentLoaded', function() {
    const dotSource = `
        digraph G {
            rankdir=TB;
            node [shape=circle, style=filled, color=lightblue, fontname="Arial"];
            edge [fontname="Arial", fontsize=10];

            Supercomputing -> Transformer [label="enables"];
            Transformer -> Reinforcement_Learning [label="enhances"];
            Reinforcement_Learning -> Planning [label="optimizes"];
            Planning -> Meta_Learning [label="aids"];
            Meta_Learning -> Fine_Tuning [label="improves"];
            Transformer -> Diffusion_Models [label="powers"];
            Transformer -> GANs [label="used in"];
            Transformer -> RAG [label="integrates with"];
            GANs -> NeRFs [label="applies to"];
            NeRFs -> 3D_Convergence [label="advances"];
            Diffusion_Models -> High_Dimensionality [label="requires"];
            Multimodal -> High_Dimensionality [label="operates in"];
            Multimodal -> Context [label="builds"];
            RAG -> Context [label="augments"];
            Compression -> Transformer [label="optimizes"];
            Compression -> High_Dimensionality [label="reduces"];
            Distillation -> Transformer [label="applies to"];
            Distillation -> Compression [label="related to"];
            Distillation -> Fine_Tuning [label="precedes"];
        }
    `;

    const viz = new Viz();
    
    viz.renderSVGElement(dotSource)
        .then(element => {
            document.getElementById("graph").appendChild(element);
        })
        .catch(error => {
            console.error("Error rendering graph:", error);
        });
});
