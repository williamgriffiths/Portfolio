const downloadButtons = document.querySelectorAll('.download-btn');

downloadButtons.forEach((button, index) => {
    button.addEventListener('click', () => {
        let sourceCodePath;
        if (index === 0) {
            sourceCodePath = 'https://github.com/williamgriffiths/portfolio/raw/main/code/1.%20GUI%20Sorting%20Algorithms/GUISorts.zip';
        } else if (index === 3) {
            sourceCodePath = 'https://raw.githubusercontent.com/williamgriffiths/portfolio/main/code/2.%20TVM%20Calculator/TVM.py';
        } else if (index === 4) {
            sourceCodePath = 'https://raw.githubusercontent.com/williamgriffiths/portfolio/main/code/3.%20Stock%20Portfolio%20Tracker/Portfolio%20Tracker.py';
        } else if (index === 5) {
            sourceCodePath = 'https://raw.githubusercontent.com/williamgriffiths/portfolio/main/code/4.%20NPV%20and%20IRR%20Calculator/NPV_IRR.py';
        } else if (index === 9) {
            sourceCodePath = 'https://raw.githubusercontent.com/williamgriffiths/portfolio/main/code/5.%20Sudoku/Sudoku%20Solver.py';
        } else if (index == 12) {
            sourceCodePath = 'https://github.com/williamgriffiths/portfolio/raw/main/group-projects/Engineering%201/auber-master.zip';
        } else if (index == 13) {
            sourceCodePath = 'https://github.com/williamgriffiths/portfolio/raw/main/group-projects/Engineering%201/ENG1%20Writeup.pdf';
        } else if (index == 14) {
            sourceCodePath = 'https://github.com/williamgriffiths/portfolio/raw/main/group-projects/Intelligent%20Systems%202/INT2-sourcecode.zip';
        } else if (index == 15) {
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
