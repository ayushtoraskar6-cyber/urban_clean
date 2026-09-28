export function getTerminalHtml(title, command, output) {
    const escapedOutput = output
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');

    return `<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>${title}</title>
    <style>
        body {
            margin: 0;
            padding: 30px;
            background: #0d1117;
            font-family: 'Consolas', 'Courier New', monospace;
            color: #c9d1d9;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 90vh;
        }
        .window {
            width: 95%;
            max-width: 1100px;
            background: #161b22;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
            border: 1px solid #30363d;
            overflow: hidden;
        }
        .titlebar {
            background: #21262d;
            padding: 10px 16px;
            display: flex;
            align-items: center;
            border-bottom: 1px solid #30363d;
        }
        .dots {
            display: flex;
            gap: 8px;
            margin-right: 16px;
        }
        .dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }
        .dot-red { background: #ff5f56; }
        .dot-yellow { background: #ffbd2e; }
        .dot-green { background: #27c93f; }
        .title {
            font-size: 13px;
            color: #8b949e;
            font-weight: 600;
            flex: 1;
            text-align: center;
        }
        .content {
            padding: 24px;
            font-size: 13px;
            line-height: 1.5;
            white-space: pre-wrap;
            word-break: break-all;
            max-height: 680px;
            overflow-y: auto;
        }
        .prompt {
            color: #58a6ff;
            font-weight: bold;
            margin-bottom: 14px;
        }
        .prompt span {
            color: #7ee787;
        }
        .output {
            color: #e6edf3;
        }
        .pass-tag {
            color: #3fb950;
            font-weight: bold;
        }
        .highlight {
            color: #f0883e;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="window">
        <div class="titlebar">
            <div class="dots">
                <div class="dot dot-red"></div>
                <div class="dot dot-yellow"></div>
                <div class="dot dot-green"></div>
            </div>
            <div class="title">${title}</div>
        </div>
        <div class="content">
            <div class="prompt">PS D:\\Urban clean&gt; <span>${command}</span></div>
            <div class="output">${escapedOutput}</div>
        </div>
    </div>
</body>
</html>`;
}
