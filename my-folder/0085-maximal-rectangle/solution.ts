function maximalRectangle(matrix: string[][]): number {

    const getLargestRectangleInHistogram = (histogram: number[]) => {
        interface data {
            startIndex: number;
            height: number;
        }

        let largestRectangle = 0;
        const stack: data[] = [];
        for (let i = 0; i < histogram.length; i++) {
            const currentHeight = histogram[i]
            if (stack.length == 0 || stack[stack.length - 1].height < currentHeight) {
                const newData: data = {startIndex: i, height: currentHeight}
                stack.push(newData);
            } else {
                let newStartIndex = i;
                while (stack.length > 0 && stack[stack.length - 1].height >= currentHeight) {
                    const poppedData = stack.pop();
                    const width = i - poppedData.startIndex;
                    const height = poppedData.height;
                    largestRectangle = Math.max(width * height, largestRectangle);
                    newStartIndex = poppedData.startIndex;
                }
                const newData: data = {startIndex: newStartIndex, height: currentHeight}
                stack.push(newData);
            }
        }
        while (stack.length > 0) {
            const poppedData = stack.pop();
            const width = histogram.length - poppedData.startIndex;
            const height = poppedData.height;
            largestRectangle = Math.max(width * height, largestRectangle);
        }
        return largestRectangle;
    }

    const matrixHeight = matrix.length;
    const matrixWidth = matrix[0].length;
    let maxRectangle = 0;
    for (let row = 0; row < matrixHeight; row++) {
        const histogram: number[] = [];
        for (let col = 0; col < matrixWidth; col++) {
            let rowPointer = row;
            let height = 0;
            while (rowPointer >= 0) {
                if (matrix[rowPointer][col] === "1") {
                    height++;
                    rowPointer--;
                } else {
                    break;
                }
            }
            histogram[col] = height;
        }
        const largestRectangleInHistogram = getLargestRectangleInHistogram(histogram);
        maxRectangle = Math.max(maxRectangle, largestRectangleInHistogram)
    }
    return maxRectangle;
};
