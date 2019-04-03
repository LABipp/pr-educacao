## Políticas Públicas de Educação e Regulação do Ensino Básico no Rio de Janeiro 

### About the research

This project is being developed by [LAB.ipp](https://github.com/LABFGV), a organization of students form FGV-Rio who believes that, with great evidence, we can improve the public sector; and prof. Carlos Ragazzo, our partner of [Todos pela Educação](https://www.todospelaeducacao.org.br).

Our goal is to **identify the singularities and issues in municipal schools of Rio de Janeiro over the years**, crossing data from the oficial indicator of performance, [IDEB](http://portal.inep.gov.br/ideb), other socioconomics indicators and laws governing municipal education.

### Results

To see the map with IDEB marks from all municipal schools in Rio, you can open the file `ideb_kepler.json` on [kepler.gl](https://kepler.gl) (the data goes from 2005 until 2017).

### Data sources

- Shapefile: [Escolas Municipais - GeoOpenData - Cidade do Rio de Janeiro](http://hub.arcgis.com/datasets/PCRJ::escolas-municipais);
- IDEB data: [Resultados - INEP: Planilhas do Ideb > Escolas > Ensino Fundamental Regular - Anos Iniciais](http://portal.inep.gov.br/web/guest/educacao-basica/ideb/resultados).

### Project Organization

    ├── LICENSE
    ├── README.md                  <- The top-level README for developers using this project (also know as this file!)
    ├── data
    │   ├── output                 <- Output processed data
    │   ├── treated                <- Clean and treated data for analysis
    │   └── raw                    <- The original, immutable data dump
    ├── code
    │   ├── notebooks              <- Jupyter notebooks
    │   └── requirements.txt       <- Packages used in the code

- The `data` folder was ommited because it can be to heavy. Instead, we have a `data.zip` compressed file of the folder, that you can open on your local :)

### Getting Started

#### Prerequisites

To run the notebbooks, you need to have the packages on `requirements.txt` installed. To do that, open the terminal and run:

```
pip3 install -U -r requirements.txt
```

### Authors

* **Fernanda Scovino** - *Code maker* - [fernandascovino](https://github.com/fernandascovino)
* **Guilherme Almeida** - *Code maker* 

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.

### Acknowledgments

* This README was adapted from [*A template to make good README.md*](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* The structure of this repository was adapted from [*Fast Project Templates*](https://github.com/JoaoCarabetta/project-templates)
