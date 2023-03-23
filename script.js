const downloadButtons = document.querySelectorAll('.download-btn');

downloadButtons.forEach((button, index) => {
    button.addEventListener('click', () => {
        let sourceCodePath;
        if (index === 0) {
            sourceCodePath = 'Code/1. GUI Sorting Algorithms/GUI_Sorting_Algorithms.zip';
        } else if (index === 1) {
            sourceCodePath = 'Code/2. TVM Calculator/TVM.py';
        } else if (index === 2) {
            sourceCodePath = 'Code/3. Stock Portfolio Tracker/Portfolio Tracker.py';
        } else if (index === 3) {
            sourceCodePath = 'Code/4. NPV and IRR Calculator/NPV_IRR.py';
        } else if (index === 4) {
            sourceCodePath = 'Code/5. Sudoku/Sudoku Solver.py';
        } else {
            sourceCodePath = `path/to/project${index + 1}-source-code.zip`;
        }
        const link = document.createElement('a');
        link.href = sourceCodePath;
        link.download = true;
        link.click();
    });
});