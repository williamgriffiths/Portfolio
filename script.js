const downloadButtons = document.querySelectorAll('.download-btn');

downloadButtons.forEach((button, index) => {
    button.addEventListener('click', () => {
        let sourceCodePath;
        if (index === 0) {
            sourceCodePath = 'https://github.com/williamgriffiths/portfolio/raw/main/code/CS/1.%20GUI%20Sorting%20Algorithms/GUISorts.zip';
        } else if (index === 3) {
            sourceCodePath = 'https://github.com/williamgriffiths/portfolio/raw/main/code/Finance/2.%20GUI%20TVM%20Calculator/gui-tvm.zip';
        } else if (index === 4) {
            sourceCodePath = 'https://github.com/williamgriffiths/portfolio/raw/main/code/Finance/3.%20Stock%20Portfolio%20Tracker/portfolio-tracker.zip';
        } else if (index === 5) {
            sourceCodePath = 'https://raw.githubusercontent.com/williamgriffiths/portfolio/main/code/Finance/4.%20NPV%20and%20IRR%20Calculator/NPV_IRR.py';
        } else if (index === 6) {
            sourceCodePath = 'https://raw.githubusercontent.com/williamgriffiths/portfolio/main/code/Misc/5.%20Sudoku/Sudoku%20Solver.py';
        } else if (index === 7) {
            sourceCodePath = 'https://raw.githubusercontent.com/williamgriffiths/portfolio/main/code/Misc/6.%20Damien%20Hirst%20Spots/spots.py';
        } else if (index == 9) {
            sourceCodePath = 'https://github.com/williamgriffiths/portfolio/raw/main/group-projects/Engineering%201/auber-master.zip';
        } else if (index == 10) {
            sourceCodePath = 'https://github.com/williamgriffiths/portfolio/raw/main/group-projects/Engineering%201/ENG1%20Writeup.pdf';
        } else if (index == 11) {
            sourceCodePath = 'https://github.com/williamgriffiths/portfolio/raw/main/group-projects/Intelligent%20Systems%202/INT2-sourcecode.zip';
        } else if (index == 12) {
            sourceCodePath = 'https://github.com/williamgriffiths/portfolio/raw/main/group-projects/Intelligent%20Systems%202/CIFAR-10%20Image%20Classification%20using%20PyTorch.pdf';
        } else {
            sourceCodePath = `path/to/project${index + 1}-source-code.zip`;
        }
        const link = document.createElement('a');
        link.href = sourceCodePath;
        link.download = true;
        link.click();
    });
});
