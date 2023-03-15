const downloadButtons = document.querySelectorAll('.download-btn');

downloadButtons.forEach((button, index) => {
    button.addEventListener('click', () => {
        const sourceCodePath = `path/to/project${index + 1}-source-code.zip`;
        const link = document.createElement('a');
        link.href = sourceCodePath;
