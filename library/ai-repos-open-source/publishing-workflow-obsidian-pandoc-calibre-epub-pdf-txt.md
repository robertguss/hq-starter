---
tags:
  - library
title: "Publishing Workflow: Obsidian, Pandoc, Calibre: EPUB, PDF, TXT"
url: "https://gist.github.com/zsviczian/db6c41d3698b13ed78f8e4f226706113"
company: [personal]
topics: []
created: 2025-04-22
source_type: raindrop
raindrop_id: 1020552460
source_domain: "gist.github.com"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-20
hydrated_via: github-gist-api
---
## Excerpt

Publishing Workflow: Obsidian, Pandoc, Calibre: EPUB, PDF, TXT - Process - Build Book.md

## Raw Content

<!-- Hydrated 2026-04-20 via github-gist-api -->

> **Gist description:** Publishing Workflow: Obsidian, Pandoc, Calibre: EPUB, PDF, TXT

> **Owner:** [zsviczian](https://gist.github.com/zsviczian/db6c41d3698b13ed78f8e4f226706113)
> **Created:** 2025-04-19T12:05:58Z · **Updated:** 2026-03-21T22:17:11Z

### `Process - Build Book.md`

```markdown
<%* /*
```js */
/**
 * Obsidian Templater script to build a book from markdown files.
 * 
 * This script automates the process of generating a publish-ready book from a set of Obsidian markdown files.
 * It is designed to work on both Windows and Mac, and can be run from within Obsidian using the Templater plugin.
 * 
 * The script performs the following steps:
 *   1. Expands all Obsidian embeds and links, recursively flattening the book structure into two markdown files:
 *      - One for Kindle (with Obsidian links converted to markdown links)
 *      - One for Paperback (with Obsidian links as plain text)
 *   2. Converts the expanded markdown files to EPUB format using Pandoc, applying custom metadata, CSS, and Lua filters.
 *   3. Generates a plain text version of the book.
 *   4. Patches the generated EPUB files to fix navigation, add ISBNs, and correct encoding issues.
 *   5. Converts the Paperback EPUB to a print-ready PDF using Calibre's ebook-convert, with custom page size, fonts, and footer.
 *   6. Opens the generated PDF in the system's default PDF viewer.
 * 
 * Prerequisites:
 *   - Pandoc must be installed: https://pandoc.org/installing.html
 *   - Calibre (for ebook-convert) must be installed: https://calibre-ebook.com/download
 *   - The supporting code directory must contain:
 *       - metadata-kindle.yaml: metadata for Kindle EPUB
 *       - metadata-paperback.yaml: metadata for Paperback EPUB
 *       - export.lua: Lua filter for Pandoc
 *       - book.css: base CSS for the book
 *       - book-kindle.css: extra CSS for Kindle
 *       - book-paperback.css: extra CSS for Paperback
 *       - fonts/: folder with TTF font files
 * 
 * Usage:
 *   - Open the root markdown file of your book in Obsidian.
 *   - Run this script using the Templater plugin.
 *   - The script will output all generated files to the configured OUTPUT_DIR.
 * 
 * Output files:
 *   - Expanded-Kindle.md: flattened markdown for Kindle
 *   - Expanded-Paperback.md: flattened markdown for Paperback
 *   - Expanded-Audiobook.md: flattened markdown for Audiobook (images replaced with alt-text for narration)
 *   - <root filename>-Kindle.epub: EPUB for Kindle
 *   - <root filename>-Paperback.epub: EPUB for Paperback
 *   - <root filename>-Audiobook.epub: EPUB for Audiobook
 *   - <root filename>-Paperback.pdf: Print-ready PDF for Paperback
 *   - <root filename>.txt: Plain text version of the book
 * 
 * Configuration:
 *   - Adjust OUTPUT_DIR and SUPPORTING_CODE_DIR as needed for your environment.
 *   - Set the paths to Pandoc and ebook-convert if they are not in your system PATH.
 *   - Update ISBN_PAPERBACK and ISBN_KINDLE as appropriate for your publication.
 */

// --- Early exit if running on mobile (not supported) ---
if (app.isMobile) return;

// --- Node.js and OS modules ---
const isWindows = process.platform === "win32";
const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');




// ------------------------------
// --- Configurable variables ---
// ------------------------------

// --- Path to binaries (edit as needed) ---
// If Pandoc or ebook-convert are not in your PATH, set the full path here.
const PANDOC_PATH = isWindows ? "pandoc" : "/opt/homebrew/bin/pandoc";
const EBOOK_CONVERT_PATH = isWindows ? "ebook-convert" : "/Applications/calibre.app/Contents/MacOS/ebook-convert"; 

// --- Output and supporting code directories ---
// OUTPUT_DIR: Where all generated files will be placed.
// SUPPORTING_CODE_DIR: Where metadata, CSS, Lua, and fonts are stored.
const OUTPUT_DIR = isWindows ? "F:\\Sketch Your Mind" : "/Users/zsviczian/Sketch Your Mind";
const SUPPORTING_CODE_DIR = isWindows ? "C:\\Users\\Zsolt\\GitHub\\Beyond-Text\\Pandoc" : "/Users/zsviczian/GitHub/Beyond-Text/Pandoc";

// --- ISBNs for different formats ---
// Set ISBN to null if you don't want to include it in the EPUB title page.
const ISBN_PAPERBACK = "978-615-02-3320-8";
const ISBN_KINDLE = "978-615-02-3323-9";

// --- Get the active file in Obsidian ---
// This is the root markdown file for your book.
const f = app.workspace.activeLeaf?.view?.file;
if (!f) {
  new Notice("No active file found! Open the root of the book you want to convert", 0);
  return;
}
const inputFile = await app.vault.adapter.getFullRealPath(f.path);
const inputFileName = path.basename(inputFile, path.extname(inputFile));
const rootDir = path.dirname(inputFile);

// --- Output file paths ---
const expandedFileKindle = path.join(OUTPUT_DIR, `${inputFileName}-Expanded-Kindle.md`);
const expandedFilePaperback = path.join(OUTPUT_DIR, `${inputFileName}-Expanded-Paperback.md`);
const expandedFileAudiobook = path.join(OUTPUT_DIR, `${inputFileName}-Expanded-Audiobook.md`);
const epubPathKindle = path.join(OUTPUT_DIR, `${inputFileName}-Kindle.epub`);
const epubPathPaperback = path.join(OUTPUT_DIR, `${inputFileName}-Paperback.epub`);
const epubPathAudiobook = path.join(OUTPUT_DIR, `${inputFileName}-Audiobook.epub`);
const textPath = path.join(OUTPUT_DIR, `${inputFileName}.txt`);
const pdfPath = path.join(OUTPUT_DIR, `${inputFileName}-Paperback.pdf`);
const tempDir = path.join(OUTPUT_DIR, "temp-epub");

// --- Supporting code paths ---
// These files must exist in SUPPORTING_CODE_DIR. Set to null to skip.
const metaKindle = path.join(SUPPORTING_CODE_DIR, "metadata-kindle.yaml");
const metaPaperback = path.join(SUPPORTING_CODE_DIR, "metadata-paperback.yaml");
const metaTxt = path.join(SUPPORTING_CODE_DIR, "metadata-kindle.yaml");
const exportLua = path.join(SUPPORTING_CODE_DIR, "export.lua");
const cssBook = path.join(SUPPORTING_CODE_DIR, "book.css");
const cssKindle = path.join(SUPPORTING_CODE_DIR, "book-kindle.css");
const cssPaperback = path.join(SUPPORTING_CODE_DIR, "book-paperback.css");
const fontsDir = path.join(SUPPORTING_CODE_DIR, "fonts", "*.ttf");

// --- PDF footer template ---
// This HTML/JS snippet is injected into the PDF footer by ebook-convert.
// It handles page numbers, chapter titles, and custom formatting.
const footerTemplate = `<footer>
  <div id='pagenum'></div>
  <script>
    var pageNum = _PAGENUM_;
    var displayNum = '';
    var section = '_SECTION_';
    var title = '_TITLE_';
    
    switch(section) {
      case 'Chapter 1': section = 'A New Paradigm for Thinking'; break;
      case 'Chapter 2': section = 'The LEGO Approach to Playful Thinking'; break;
      case 'Chapter 3': section = 'Notes Reimagined'; break;
      case 'Chapter 4': section = 'Visualizing Concepts'; break;
      case 'Chapter 5': section = 'Mapping the Mind'; break;
      case 'Chapter 6': section = 'The Idea Integration Board'; break;
      case 'Chapter 7': section = 'Navigating Knowledge'; break;
      case 'Chapter 8': section = 'The Serendipity Machine'; break;
      case 'Chapter 9': section = 'Trains of Thought'; break;
      case 'Chapter 10': section = 'Create Thinking Loops with Storyboards'; break;
      case 'Chapter 11': section = 'Flip the Habit and Free the Genie'; break;
    }
    
    /* Determine displayed page number format */
    if (pageNum <= 11) {
      /* No page number for the first 5 pages */
      displayNum = '';
    } else if (pageNum >= 12 && pageNum <= 22) {
      /* Roman numerals for pages 6-22 */
      var romanNumerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII'];
      displayNum = romanNumerals[pageNum];
    } else {
      /* Arabic numerals starting from page 20 (displayed as 1) */
      displayNum = (pageNum - 22).toString();
    }

    var isTitle = [11, 14, 15, 22, 23, 37, 51, 65, 71, 72, 73, 93, 116, 117, 128, 129, 149, 164, 165, 186, 187, 198, 199, 215, 219, 227, 231, 239].includes(pageNum);
    if(isTitle) {
      displayNum = '';
    }

    if(displayNum) {
      if(pageNum % 2 == 0) {
        displayNum = displayNum + '<span style=\\'margin-left:1.2em;\\'>' + title.toLocaleUpperCase() + '</span>';
      } else {
        displayNum = '<span style=\\'margin-right:1.2em;\\'>' + section.toLocaleUpperCase() + '</span>' + displayNum;
      }
    }
    var div = document.currentScript.parentNode.querySelector('#pagenum');
    div.style.fontFamily = 'Fira Sans';
    div.style.fontSize = '0.9em';
    div.style.width = '100%';
    div.style.textAlign = pageNum % 2 ? 'right' : 'left';
    div.innerHTML = displayNum;
  </script>
</footer>`;




// -------------------------
// --- Utility functions ---
// -------------------------

// --- Single notice management ---
// Use a single persistent notice for status updates (not errors).
let notice;
let noticeEl;
function setSingleNotice(message) {
    if(noticeEl?.parentElement) {
        notice.setMessage(message);
        return;
    }
    // 0 means the notice will not be automatically removed
    notice = new Notice(message, 0);
    noticeEl = notice.containerEl ?? notice.noticeEl;
}
function hideSingleNotice() {
    if(noticeEl?.parentElement) {
        notice.hide();
    }
}

// --- PDF viewer management ---
// Detects and closes the default PDF viewer before build, and opens the PDF after build.
// This is necessary to avoid issues with file locks and to ensure the latest version is opened.
async function getDefaultPdfViewer() {
  if (isWindows) {
    // Step 1: Get default ProgID from HKLM
    const cmd = `powershell -command "(Get-ItemProperty 'HKLM:\\SOFTWARE\\Classes\\.pdf').'(default)'"`;
    let { ok, stdout } = await runCmd(cmd);
    if (ok && stdout.trim()) {
      const progId = stdout.trim();

      // Step 2: Get associated open command
      const exeCmd = `powershell -command "(Get-ItemProperty 'HKLM:\\SOFTWARE\\Classes\\${progId}\\shell\\open\\command').'(default)'"`;
      const { ok: exeOk, stdout: exeStdout } = await runCmd(exeCmd);
      if (exeOk && exeStdout.trim()) {
        const match = exeStdout.match(/"([^"]+)"/);
        return match ? match[1] : null;
      }
    }
    // Fallback to common PDF viewers
    const commonViewers = [
      "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe",
      "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe",
      "C:\\Program Files\\SumatraPDF\\SumatraPDF.exe"
    ];
    
    for (const viewer of commonViewers) {
      if (fs.existsSync(viewer)) {
        return viewer;
      }
    }
  } else {
    // macOS default PDF viewer detection
    const cmd = "defaults read com.apple.LaunchServices/com.apple.launchservices.secure LSHandlers | grep -A 3 'LSHandlerURLScheme = pdf' | grep 'LSHandlerRoleAll' | awk -F '=' '{print $2}' | tr -d ' ;'";
    const { ok, stdout } = await runCmd(cmd);
    if (ok && stdout.trim()) {
      const appId = stdout.trim();
      if (appId === "com.apple.preview") {
        return "/Applications/Preview.app/Contents/MacOS/Preview";
      } else if (appId === "com.adobe.Reader") {
        return "/Applications/Adobe Acrobat Reader DC.app/Contents/MacOS/AdobeReader";
      } else if (appId.includes("adobe")) {
        return "/Applications/Adobe Acrobat DC.app/Contents/MacOS/Acrobat";
      }
    }
    // Fallback to common macOS PDF viewers
    const commonViewers = [
      "/Applications/Preview.app/Contents/MacOS/Preview",
      "/Applications/Adobe Acrobat DC.app/Contents/MacOS/Acrobat",
      "/Applications/Adobe Acrobat Reader DC.app/Contents/MacOS/AdobeReader"
    ];
    
    for (const viewer of commonViewers) {
      if (fs.existsSync(viewer)) {
        return viewer;
      }
    }
  }
  return null;
}

async function closePdfViewer() {
  const pdfViewer = await getDefaultPdfViewer();
  if (!pdfViewer) {
    setSingleNotice("Couldn't determine PDF viewer application");
    return;
  }
  
  const viewerName = path.basename(pdfViewer, path.extname(pdfViewer));
  setSingleNotice(`Closing any running instances of ${viewerName}...`);
  
  if (isWindows) {
    const cmd = `taskkill /F /IM "${path.basename(pdfViewer)}" /T`;
    await runCmd(cmd, {}, true);
  } else {
    const cmd = `pkill -f "${viewerName}"`;
    await runCmd(cmd, {}, true);
  }
}

async function openPdf(pdfPath) {
  if (!fs.existsSync(pdfPath)) {
    setSingleNotice(`PDF file not found: ${pdfPath}`);
    return false;
  }

  setSingleNotice(`Opening PDF: ${path.basename(pdfPath)}`);
  let cmd;
  
  if (isWindows) {
    cmd = `start "" "${pdfPath}"`;
  } else {
    cmd = `open "${pdfPath}"`;
  }
  
  const { ok } = await runCmd(cmd);
  return ok;
}

// --- Shell command runner ---
// Runs a shell command and returns a promise with {ok, stdout, stderr}.
// Shows warnings as notices, but errors as persistent notices.
async function runCmd(cmd, opts = {}, hideError = false) {
  return new Promise((resolve) => {
    const execOptions = {...opts};
    
    exec(cmd, execOptions, (error, stdout, stderr) => {
      if (!hideError && error) {
        new Notice(`Error: ${error.message}`, 0);
        resolve({ ok: false, stdout, stderr });
      } else if (!hideError && stderr) {
        // Check if stderr contains only warnings using a simpler pattern
        const isOnlyWarning = stderr.match(/warning/i);
        
        if (isOnlyWarning) {
          // Just log the warning but don't treat as failure
          setSingleNotice(`Warning: ${stderr}`);
          resolve({ ok: true, stdout, stderr });
        } else {
          // Actual error in stderr
          new Notice(`Stderr: ${stderr}`, 0);
          resolve({ ok: false, stdout, stderr });
        }
      } else {
        resolve({ ok: true, stdout, stderr });
      }
    });
  });
}


// --- Check if required binaries are available ---
// Used to validate that pandoc and ebook-convert are installed and accessible.
async function checkBinary(bin) {
  const whichCmd = isWindows ? `where ${bin}` : `which ${bin}`;
  const { ok } = await runCmd(whichCmd);
  if (!ok) {
    new Notice(`Required binary not found: ${bin}`, 0);
    return false;
  }
  return true;
}




// ----------------------------------------
// --- Step 0: Check for required files ---
// ----------------------------------------

// Verify that the required binaries are available
const bins = [PANDOC_PATH, EBOOK_CONVERT_PATH];
for (const bin of bins) {
  if (!(await checkBinary(bin))) return;
}
// Ensure OUTPUT_DIR exists before proceeding
if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}
// Ensure SUPPORTING_CODE_DIR exists before proceeding
if (!fs.existsSync(SUPPORTING_CODE_DIR)) {
  new Notice(`Supporting code directory not found: ${SUPPORTING_CODE_DIR}`, 0);
  return;
}

// Close PDF viewer before starting the process
// This is necessary to avoid file locks and
// ensure the latest version is opened.
await closePdfViewer();




// ---------------------------------------------
// --- Step 1: Expand Obsidian Links/Embeds ---
// ---------------------------------------------

// Recursively expands all Obsidian embeds and links in the root markdown file.
// Produces two outputs: one for Kindle (links as markdown), one for Paperback (links as plain text).
async function expandObsidianLinks(inputFile, outputFileKindle, outputFilePaperback, outputFileAudiobook) {
  setSingleNotice("Step 1: Expanding Obsidian links...");
  
  // Create the Obsidian Vault adapter for file access
  const processedFiles = new Set();
 
  /**
   * 
   * @param {*} filePath 
   * @param {*} targetFormat "kindle" | "paperback" | "audiobook"
   * @returns 
   */
  async function processMarkdownFile(filePath, targetFormat) {
    // Avoid infinite loops
    if (processedFiles.has(filePath)) {
      const output = `\n<!-- Skipping duplicate embed: ${filePath} -->\n`;
      return output;
    }
    
    processedFiles.add(filePath);
    
    try {
      // Read file content
      const content = await fs.promises.readFile(filePath, 'utf8');
      const contentLines = content.split(/\r?\n/);
      
      // Check if this is a TOC file by examining frontmatter
      let hasFrontmatter = contentLines.length > 2 && contentLines[0] === "---";
      let isTocFile = false;
      
      if (hasFrontmatter) {
        let frontmatterEndIndex = -1;
        
        // Find the closing --- of frontmatter
        for (let i = 1; i < contentLines.length; i++) {
          if (contentLines[i] === "---") {
            frontmatterEndIndex = i;
            break;
          }
        }
        
        if (frontmatterEndIndex > 0) {
          // Look for aliases: and Table of Contents in frontmatter
          const frontmatter = contentLines.slice(0, frontmatterEndIndex + 1);
          const hasAliases = frontmatter.some(line => line.match(/aliases:/));
          const hasTocAlias = frontmatter.some(line => line.match(/- "Table of Contents"/));
          
          if (hasAliases && hasTocAlias) {
            isTocFile = true;
          }
        }
      }
      
      let insideAbstract = false;
      let result = [];
      
      for (const line of contentLines) {
        // Process headings to convert to uppercase properly
        if (line.match(/^##\s+(.+)$/)) {
          const heading = line.replace(/^##\s+/, "");
          const uppercaseHeading = heading.replace(/([a-z])/g, (match) => match.toUpperCase());
          result.push(`## ${uppercaseHeading}`);
          continue;
        } 
        else if (line.match(/^###\s+(.+)$/)) {
          const heading = line.replace(/^###\s+/, "");
          const uppercaseHeading = heading.replace(/([a-z])/g, (match) => match.toUpperCase());
          result.push(`### ${uppercaseHeading}`);
          continue;
        }
        
        // Transform Example and Mastery callout blocks
        // I use multiple different callout blocks
        // these are pre-processed in export.lua
        // the logic here is only additional transformation to extend specific callouts
        // with additional text (e.g., "Example" or "Pro Tip")

        /**
         * If the prefix does not match the function does nothing.
         * @param {*} line markdown line to process
         * @param {*} prefix callout prefix (e.g., "Example", "Mastery", "Abstract")
         * @param {*} suffix text to append to the callout (e.g., "Example", "Pro Tip")
         */
        function processCallout(line, prefix, suffix) {
          let calloutMatch = line.match(new RegExp(`^>\\s*\\[!${prefix}\\]\\s+(.+)$`));
          if (calloutMatch) {
            if(suffix) {
              result.push(`> [!${prefix}] ${suffix}: ${calloutMatch[1]}`);
            } else {
              result.push(`> [!${prefix}] ${calloutMatch[1]}`);
            }
            return true;
          }

          if (line.match(new RegExp(`^>\\s*\\[!${prefix}\\]\\s*$`))) {
            if(suffix) {
              result.push(`> [!${prefix}] ${suffix}`);
            } else {
              result.push(`> [!${prefix}]`);
            }
            return true;
          }
          return false;
        }

        if (
          processCallout(line, "Example", "Example") ||
          processCallout(line, "Mastery", "Pro Tip")
        ) {
          continue;
        }
        
        if (
          targetFormat === "audiobook" && (
            processCallout(line, "Story", "Storytime") ||
            processCallout(line, "Definition", "Definition") ||
            processCallout(line, "Practice", "Practice") ||
            processCallout(line, "Takeaway", "Key Takeaways")
          )
        ) {
          continue; 
        }

        if (processCallout(line, "Abstract")) {
          insideAbstract = true;
          continue;
        };
        
        // Insert page break AFTER [!Abstract] (after the first blank line following it)
        if (insideAbstract && line.match(/^\s*$/)) {
          result.push(line);
          result.push('<div style="page-break-after: always"></div>');
          result.push('');
          insideAbstract = false;
          continue;
        }
        
        // Only transform Obsidian links in TOC file
        if (isTocFile && line.includes("[[")) {
          let transformedLine = line;
          let matches = [...line.matchAll(/\[\[(.+?)(?:\|(.+?))?\]\]([^\n]*)/g)];
          
          if (matches.length > 0) {
            transformedLine = "";
            let lastIndex = 0;
            
            for (const match of matches) {
              // Add text before the match
              transformedLine += line.substring(lastIndex, match.index);
              
              const linkedFile = match[1];
              const displayText = match[2] || linkedFile;
              
              // Use the display text to generate anchor IDs (same way Pandoc does)
              let anchor = displayText.toLowerCase();
              anchor = displayText.split(':', 2)[0].trim().toLowerCase();
              
              // Special cases for consistent hyphenation
              anchor = anchor.replace("note-taking", "note-taking"); // Ensure proper hyphenation
              anchor = anchor.replace("note taking", "note-taking"); // Catch space variant too
              
              // Then apply standard transformations
              anchor = anchor.replace(/[^a-z0-9\- ]/g, ''); // Remove special chars but keep hyphens
              anchor = anchor.replace(/\s+/g, '-');         // Replace spaces with hyphens
              anchor = anchor.replace(/-+/g, '-');          // Remove duplicate hyphens
              
              // Create the transformed link
              switch (targetFormat) {
                case "kindle":
                  transformedLine += `[${displayText}](#${anchor})`;
                  break;
                case "paperback":
                  transformedLine += displayText + match[3];
                  break;
                case "audiobook":
                  transformedLine += displayText;
                  break;
              }
              
              // Update lastIndex for next iteration
              lastIndex = match.index + match[0].length;
            }
            
            // Add remaining text after the last match
            transformedLine += line.substring(lastIndex);
            result.push(transformedLine);
            continue;
          }
        }
        
        // Handle image embeds: `![[image.png|alt text|300]]` or `![[image.png||58%]]`
        const imageMatch = line.match(/^(>\s*|\s+)?\!\[\[(.+?\.(png|jpg|jpeg|gif|svg|webp))(\|([^|]*))?(\|(\d+%?))?\]\]\s*$/);
        if (imageMatch) {
          const prefix = imageMatch[1] || "";  // Capture `>` if present (for blockquotes)
          const imagePath = imageMatch[2];     // Extract image filename
          const altText = imageMatch[5] || ""; // Extract alt text (if provided)
          const width = imageMatch[7] || "";   // Extract width (if provided)
          
          // Determine width attribute format
          let widthAttr = "";
          if (width.match(/^\d+%$/)) {
            widthAttr = `{width=${width}}`;  // Percentage-based width
          } else if (width.match(/^\d+$/)) {
            widthAttr = `{width=${width}px}`;  // Pixel-based width
          }
          
          // Preserve blockquote (`>` prefix) if present
          if (targetFormat === "audiobook") {
            result.push(`${prefix} ${altText}`);
          } else {
            result.push(`${prefix}![${altText}](../images/${imagePath})${widthAttr}`);
          }
          continue;
        }
        
        // Handle Markdown file embeds recursively
        const embedMatch = line.match(/^\!\[\[(.+?)\]\]$/);
        if (embedMatch) {
          const embedText = embedMatch[1];
          
          // Remove alias part if present (e.g., "Chapter-01|The Beginning" → "Chapter-01")
          const fileName = embedText.replace(/\|.*$/, "");
          
          // Ensure file has .md extension if missing
          const fileNameWithExt = fileName.endsWith(".md") ? fileName : `${fileName}.md`;
          
          // Resolve file path
          const embeddedFilePath = path.join(rootDir, fileNameWithExt);
          
          if (await fs.promises.access(embeddedFilePath).then(() => true).catch(() => false)) {
            result.push(`\n<!-- Expanded from ${fileNameWithExt} -->\n`);
            const embedContent = await processMarkdownFile(embeddedFilePath, targetFormat);
            result.push(embedContent);
            result.push(`\n<!-- End of ${fileNameWithExt} -->\n`);
          } else {
            result.push(`\n<!-- Missing File: ${fileNameWithExt} -->\n`);
          }
          continue;
        }
        
        let processedLine = "";
        // Replace div markers
        if (targetFormat === "audiobook") {
          processedLine = line.replaceAll(/<!-- div:([a-zA-Z0-9_-]+) -->/gi, '');
          processedLine = processedLine.replaceAll(/<!-- \/div -->/gi, '');
        } else {
          processedLine = line.replaceAll(/<!-- div:([a-zA-Z0-9_-]+) -->/gi, '<div class="$1">');
          processedLine = processedLine.replaceAll(/<!-- \/div -->/gi, '</div>');
        }
        
        // Append the line to output
        result.push(processedLine);
      }
      
      return result.join('\n');
    }
    catch (err) {
      return `\n<!-- Error processing file ${filePath}: ${err.message} -->\n`;
    }
  }
  
  // Process for Kindle version
  processedFiles.clear();
  const kindleContent = await processMarkdownFile(inputFile, "kindle");
  await fs.promises.writeFile(outputFileKindle, kindleContent, 'utf8');
  setSingleNotice(`Expanded markdown saved to: ${outputFileKindle}`);
  
  // Process for Paperback version
  processedFiles.clear();
  const paperbackContent = await processMarkdownFile(inputFile, "paperback");
  await fs.promises.writeFile(outputFilePaperback, paperbackContent, 'utf8');
  setSingleNotice(`Expanded markdown saved to: ${outputFilePaperback}`);
  
  // Process for Paperback version
  processedFiles.clear();
  const audiobookContent = await processMarkdownFile(inputFile, "audiobook");
  await fs.promises.writeFile(outputFileAudiobook, audiobookContent, 'utf8');
  setSingleNotice(`Expanded markdown saved to: ${outputFileAudiobook}`);

  return true;
}




// -----------------------------------
// --- Step 2: Patch EPUB files    ---
// -----------------------------------

// Unzips the EPUB, modifies navigation, adds ISBN, fixes encoding, then repackages.
// This is a hack. I found that some changes are easier to implment in the EPUB file directly than in
// the markdown source files or the lua filters or configuring pandoc.
async function patchEpubFile(epubPath, isPaperback = false) {
  setSingleNotice(`Patching EPUB file: ${path.basename(epubPath)}...`);
  
  // Create temp directory
  if (await fs.promises.access(tempDir).then(() => true).catch(() => false)) {
    await fs.promises.rm(tempDir, { recursive: true, force: true });
  }
  await fs.promises.mkdir(tempDir, { recursive: true });
  
  // Extract EPUB
  const zipName = `${epubPath}.zip`;
  await fs.promises.copyFile(epubPath, zipName);
  
  // Use unzip for extraction
  const unzipCmd = isWindows 
      ? `powershell -command "Expand-Archive -Path '${zipName}' -DestinationPath '${tempDir}'"` 
      : `unzip -q "${zipName}" -d "${tempDir}"`;
  
  let res = await runCmd(unzipCmd);
  if (!res.ok) {
    new Notice(`Failed to extract EPUB: ${res.stderr}`, 0);
    return false;
  }
  
  // Rename back from zip
  await fs.promises.unlink(zipName);
  
  // Find and modify TOC file (only for Kindle version)
  if (!isPaperback) {
    // Find nav.xhtml recursively
    const findNavCmd = isWindows
        ? `powershell -command "Get-ChildItem -Path '${tempDir}' -Recurse -Filter 'nav.xhtml' | Select-Object -First 1 -ExpandProperty FullName"`
        : `find "${tempDir}" -name "nav.xhtml" -type f | head -1`;
    
    res = await runCmd(findNavCmd);
    if (res.ok && res.stdout.trim()) {
      const tocFile = res.stdout.trim();
      let content = await fs.promises.readFile(tocFile, 'utf8');
      const modifiedContent = content.replace('<nav epub:type="toc"', '<nav epub:type="toc" hidden="hidden"');
      await fs.promises.writeFile(tocFile, modifiedContent, 'utf8');
      setSingleNotice(`Modified TOC file: ${path.basename(tocFile)}`);
    }
  }
  
  // Find and modify the title page (title_page.xhtml)
  const findTitlePageCmd = isWindows
      ? `powershell -command "Get-ChildItem -Path '${tempDir}' -Recurse -Filter 'title_page.xhtml' | Select-Object -First 1 -ExpandProperty FullName"`
      : `find "${tempDir}" -name "title_page.xhtml" -type f | head -1`;
  
  res = await runCmd(findTitlePageCmd);
  if (res.ok && res.stdout.trim()) {
    const titlePageFile = res.stdout.trim();
    let content = await fs.promises.readFile(titlePageFile, 'utf8');
    
    // Add ISBN based on format
    const isbn = isPaperback ? ISBN_PAPERBACK : ISBN_KINDLE;
    
    if(isbn) {
      // Insert the ISBN before the rights div
      if (content.includes('<div class="rights">')) {
        const modifiedContent = content.replace(
          '<div class="rights">',
          `<p class="identifier">ISBN: ${isbn}</p>\n  <div class="rights">`
        );
        await fs.promises.writeFile(titlePageFile, modifiedContent, 'utf8');
        setSingleNotice(`Added ISBN ${isbn} to title page`);
      }
    }
  }
  
  // Find and modify the main title page (ch001.xhtml)
  const findMainTitleCmd = isWindows
      ? `powershell -command "Get-ChildItem -Path '${tempDir}' -Recurse -Filter 'ch001.xhtml' | Select-Object -First 1 -ExpandProperty FullName"`
      : `find "${tempDir}" -name "ch001.xhtml" -type f | head -1`;
  
  res = await runCmd(findMainTitleCmd);
  if (res.ok && res.stdout.trim()) {
    const mainTitleFile = res.stdout.trim();
    let content = await fs.promises.readFile(mainTitleFile, 'utf8');
    
    // Check if the file contains the main title
    if (content.includes('<h1 class="unnumbered">Sketch Your Mind</h1>')) {
      // Create the replacement string
      const replacement = '<div class="book-title">\n' +
          '<div class="book-title-main">Sketch Your Mind</div>\n' +
          '<div class="book-title-subtitle">Nurture a Playful and Creative Brain</div>\n' +
          '</div>\n' +
          '<div class="chapter-spacing"></div>';
      
      const modifiedContent = content.replace(
        '<h1 class="unnumbered">Sketch Your Mind</h1>',
        replacement
      );
      
      await fs.promises.writeFile(mainTitleFile, modifiedContent, 'utf8');
      setSingleNotice(`Modified main title file with subtitle`);
    }
  }
  
  // Fix encoding issues in all HTML files
  const findHtmlCmd = isPaperback
      ? (isWindows 
          ? `powershell -command "Get-ChildItem -Path '${tempDir}' -Recurse -Filter 'ch001.xhtml' | Select-Object -ExpandProperty FullName"`
          : `find "${tempDir}" -name "ch001.xhtml" -type f`)
      : (isWindows
          ? `powershell -command "Get-ChildItem -Path '${tempDir}' -Recurse -Filter '*.xhtml' | Select-Object -ExpandProperty FullName"`
          : `find "${tempDir}" -name "*.xhtml" -type f`);
  
  res = await runCmd(findHtmlCmd);
  if (res.ok && res.stdout.trim()) {
    const htmlFiles = res.stdout.trim().split(/\r?\n/);
    
    for (const htmlFile of htmlFiles) {
      if (!htmlFile.trim()) continue;
      
      let htmlContent = await fs.promises.readFile(htmlFile, 'utf8');
      
      // Create proper em-dash character
      const dash = "—"; // Unicode em-dash
      
      // Fix various forms of broken em-dashes
      htmlContent = htmlContent.replace(/\uFFFD/g, dash);        // Unicode replacement character
      htmlContent = htmlContent.replace(/&#65533;/g, dash);      // HTML entity for replacement character
      htmlContent = htmlContent.replace(/&amp;#65533;/g, dash);  // Doubly-encoded HTML entity
      htmlContent = htmlContent.replace(/�/g, dash);             // Visible replacement character
      
      // Fix specific patterns for section headers
      const pattern1 = '<h3><strong>STEP 1: STRUCTURAL READING';
      const replacement1 = `<h3><strong>STEP 1: STRUCTURAL READING${dash}GRASP THE WHOLE</strong></h3>`;
      htmlContent = htmlContent.replace(
        new RegExp(`${pattern1}.*?GRASP THE WHOLE</strong></h3>`),
        replacement1
      );
      
      const pattern2 = '<h3><strong>STEP 2: ITERATIVE READING';
      const replacement2 = `<h3><strong>STEP 2: ITERATIVE READING${dash}WHOLE, PART, WHOLE</strong></h3>`;
      htmlContent = htmlContent.replace(
        new RegExp(`${pattern2}.*?WHOLE, PART, WHOLE</strong></h3>`),
        replacement2
      );
      
      const pattern3 = '<h3><strong>STEP 3: ACTIVE READING';
      const replacement3 = `<h3><strong>STEP 3: ACTIVE READING${dash}UNDERSTAND AND CAPTURE</strong></h3>`;
      htmlContent = htmlContent.replace(
        new RegExp(`${pattern3}.*?UNDERSTAND AND CAPTURE</strong></h3>`),
        replacement3
      );
      
      await fs.promises.writeFile(htmlFile, htmlContent, 'utf8');
    }
  }
  
  // Pack back to EPUB
  await fs.promises.rename(epubPath, `${epubPath}.old`);
  
  // Create zip file
  const zipCmd = isWindows
      ? `powershell -command "Compress-Archive -Path '${tempDir}/*' -DestinationPath '${epubPath}.zip'"`
      : `cd "${tempDir}" && zip -q -r "${epubPath}.zip" ./*`;
  
  res = await runCmd(zipCmd);
  if (!res.ok) {
    new Notice(`Failed to create zip file: ${res.stderr}`, 0);
    await fs.promises.rename(`${epubPath}.old`, epubPath);
    return false;
  }
  
  // Rename zip to epub
  await fs.promises.rename(`${epubPath}.zip`, epubPath);
  
  // Clean up
  await fs.promises.unlink(`${epubPath}.old`);
  await fs.promises.rm(tempDir, { recursive: true, force: true });
  
  setSingleNotice(`Successfully patched: ${path.basename(epubPath)}`);
  return true;
}




// -----------------------------------
// --- Step 3: Main Build Process  ---
// -----------------------------------

try {
  // Expand all links and embeds
  await expandObsidianLinks(inputFile, expandedFileKindle, expandedFilePaperback, expandedFileAudiobook);

  // Convert expanded markdown to EPUB using Pandoc
  // Convert to Kindle EPUB
  // pandoc writer options:
  // https://pandoc.org/MANUAL.html#general-writer-options
  setSingleNotice("Step 2: Converting to EPUB with Pandoc...");
  let pandocCmd = [
    PANDOC_PATH,
    `"${expandedFileKindle}"`,
    `--from markdown+smart`,
    `--to epub3`,
    `-o "${epubPathKindle}"`,
    ...metaKindle ? [`--metadata-file "${metaKindle}"`] : [],
    ...exportLua ? [`--lua-filter="${exportLua}"`] : [],
    ...cssBook ? [`--css="${cssBook}"`] : [],
    ...cssKindle ? [`--css="${cssKindle}"`] : [],
    `--toc --toc-depth=2`,
    `--resource-path="${rootDir}"`,
    `--data-dir="${OUTPUT_DIR}"`,
    `--epub-chapter-level=1`
  ].join(" ");

  let res = await runCmd(pandocCmd, {cwd: rootDir});
  if (!res.ok) return;
  setSingleNotice(`EPUB created successfully: ${path.basename(epubPathKindle)}`);
  
  // Convert to Paperback EPUB
  pandocCmd = [
    PANDOC_PATH,
    `"${expandedFilePaperback}"`,
    `--from markdown+smart`,
    `--to epub3`,
    `-o "${epubPathPaperback}"`,
    ...metaPaperback ? [`--metadata-file "${metaPaperback}"`] : [],
    ...exportLua ? [`--lua-filter="${exportLua}"`] : [],
    ...cssBook ? [`--css="${cssBook}"`] : [],
    ...cssPaperback ? [`--css="${cssPaperback}"`] : [],
    `--toc --toc-depth=1`,
    `--resource-path="${rootDir}"`,
    `--data-dir="${OUTPUT_DIR}"`,
    `--epub-chapter-level=1`,
    ...fontsDir ? [`--epub-embed-font="${fontsDir}"`] : []
  ].join(" ");
  
  res = await runCmd(pandocCmd, {cwd: rootDir});
  if (!res.ok) return;
  setSingleNotice(`EPUB created successfully: ${path.basename(epubPathPaperback)}`);

  // Convert to Audiobook EPUB
  pandocCmd = [
    PANDOC_PATH,
    `"${expandedFileAudiobook}"`,
    `--from markdown+smart`,
    `--to epub3`,
    `-o "${epubPathAudiobook}"`,
    ...metaKindle ? [`--metadata-file "${metaKindle}"`] : [],
    ...exportLua ? [`--lua-filter="${exportLua}"`] : [],
    ...cssBook ? [`--css="${cssBook}"`] : [],
    ...cssKindle ? [`--css="${cssKindle}"`] : [],
    `--toc=false`,
    `--resource-path="${rootDir}"`,
    `--data-dir="${OUTPUT_DIR}"`,
    `--epub-chapter-level=1`
  ].join(" ");

  res = await runCmd(pandocCmd, {cwd: rootDir});
  if (!res.ok) return;

  // Generate plain text version
  setSingleNotice("Step 2b: Generating plain text version...");
  let textCmd = [
    PANDOC_PATH,
    `"${expandedFileAudiobook}"`,
    `--from markdown+smart`,
    `--to plain`,
    `-o "${textPath}"`,
    `--wrap=none`,
    ...metaTxt ? [`--metadata-file "${metaTxt}"`] : [],
    `--resource-path="${rootDir}"`,
    `--data-dir="${OUTPUT_DIR}"`
  ].join(" ");
  
  res = await runCmd(textCmd, {cwd: rootDir});
  // Continue even if text fails

  // Post-process plain text file to remove callout markers
  if (fs.existsSync(textPath)) {
    let txt = await fs.promises.readFile(textPath, "utf8");
    // Remove leading callout markers like [!Example] from each line
    txt = txt.replace(/^ *\[![^\]]+] */gm, "");
    // Replace all NBSP (Unicode \u00A0) with normal space
    txt = txt.replace(/\u00A0/g, " ");
    await fs.promises.writeFile(textPath, txt, "utf8");
  }

  // Patch EPUB files (navigation, ISBN, encoding)
  setSingleNotice("Step 3: Patching EPUB files...");
  await patchEpubFile(epubPathKindle, false);
  await patchEpubFile(epubPathPaperback, true);

  // Convert Paperback EPUB to PDF using Calibre
  // Build ebook-convert command
  // for valid parameters see:
  // https://manual.calibre-ebook.com/generated/en/ebook-convert.html#pdf-output-options
  setSingleNotice("Step 4: Converting EPUB to PDF...");
  const pdfCmd = [
    EBOOK_CONVERT_PATH,
    `"${epubPathPaperback}"`,
    `"${pdfPath}"`,
    `--custom-size 432x648`, //6" x 9" at 72dpi 6*72=432, 9*72=648
    `--unit point`,
    `--pdf-default-font-size 13`,
    `--pdf-mono-font-size 12`,
    `--pdf-serif-family "Bitter"`,
    `--pdf-sans-family "Fira Sans"`,
    `--pdf-mono-family "Fira Mono"`,
    `--pdf-standard-font serif`,
    `--pdf-page-numbers`,
    `--pdf-odd-even-offset 18`, // 18pt = 0.25"
    `--pdf-page-margin-left 42`, // 42pt = 0.583"
    `--pdf-page-margin-right 42`,
    `--pdf-page-margin-top 42`,
    `--pdf-page-margin-bottom 54`, // 54pt = 0.75"
    `--preserve-cover-aspect-ratio`,
    `--embed-all-fonts`,
    `--disable-font-rescaling`,
    ...footerTemplate ? [`--pdf-footer-template "${footerTemplate.replaceAll(/"/g, '\\"').replaceAll(/\s+/g, ' ')}"`] : [],
    `--pdf-no-cover`
  ].join(" ");

  res = await runCmd(pdfCmd);
  if (!res.ok) {
    new Notice(`PDF conversion failed: ${res.stderr}`, 0);
  } else {
    setSingleNotice(`PDF created successfully: ${path.basename(pdfPath)}`);
  }

  // Final status and open PDF
  new Notice(`All processing complete!\nFinal EPUB: ${path.basename(epubPathKindle)}\nFinal PDF: ${path.basename(pdfPath)}`, 6000);
  setTimeout(hideSingleNotice, 2000);

  if (fs.existsSync(pdfPath)) {
    await openPdf(pdfPath);
  } else {
    new Notice(`PDF file not found at ${pdfPath}`, 0);
  }
} catch (error) {
  hideSingleNotice();
  new Notice(`Error: ${error.message}`, 0);
} finally {
  // If the user selected text in the editor, return that so Templater does not delete it when inserting this template
  tR += app.workspace.activeLeaf.view.editor.getSelection();
}
/*
```
*/
%>
```

### `Readme.md`

```markdown
Project files for: [How I Published My Book for $0 Using Obsidian, Pandoc, Calibre (EPUB, PDF, Audiobook)](https://youtu.be/nYReYJQfqjI) - YouTube Walkthrough

If you find my work valuable, then please support my work on [ko-fi](https://ko-fi.com/zsolt).

These files are provided as a companion to my YouTube video demonstrating how to self-publish a book for free using Obsidian, Pandoc, and Calibre.  This gist includes:

- **CSS Stylesheets**:  `book-kindle.css`, `book-paperback.css`, and `book.css` -  Used for styling your EPUB and PDF outputs.
- **LUA Filter**: `export.lua` - A Pandoc filter for custom processing of callouts and chapter headers.
- **Templater Script**: `Process - Build Book.md` - An Obsidian Templater script to automate the entire book generation process.
- **YAML Metadata**: `metadata-kindle.yaml` - Example metadata for your book.

To use these files, you'll need to have the following tools installed and configured:

- **Elevenlabs**: [https://elevenlabs.io/](https://elevenlabs.io/) (For Audiobook generation - optional and not fully covered in these files. See video for details.)
- **Pandoc**: [https://pandoc.org/installing.html](https://pandoc.org/installing.html) -  Must be installed and accessible in your system's PATH.
    - [Pandoc document writer options](https://pandoc.org/MANUAL.html#general-writer-options) (For advanced customization)
- **Calibre**: [https://calibre-ebook.com/download](https://calibre-ebook.com/download) - Must be installed and `ebook-convert` accessible in your system's PATH.
    - [Calibre PDF options](https://manual.calibre-ebook.com/generated/en/ebook-convert.html#pdf-output-options) (For advanced PDF customization)
- **Obsidian**: [https://Obsidian.md](https://Obsidian.md)
- **Obsidian Excalidraw Plugin**: [https://github.com/zsviczian/obsidian-excalidraw-plugin/](https://github.com/zsviczian/obsidian-excalidraw-plugin/)

**Important Notes:**

- **Image Folder Structure**: The provided Templater script assumes your book project follows this folder structure:
    ```
    Book Project
    ├── chapters
    │   ├── Chapter-1.md
    │   ├── Chapter-2.md
    │   └── ...
    └── images
        ├── image-1.png
        ├── image-2.png
        └── ...
    ```
    Place your chapter Markdown files in the `chapters` folder and your images in the `images` folder, both within the main "Book Project" folder. The script expects the `images` folder to be located next to the `chapters` folder.

- **Customization**: These files are provided as a starting point. You will likely need to customize the CSS, LUA filter, and Templater script to match your specific book formatting and workflow requirements. Refer to the video and the linked documentation for Pandoc and Calibre for customization options.

- **Elevenlabs**: Audiobook generation is mentioned in the video, but the included scripts primarily focus on EPUB and PDF creation.  Audiobook generation is a more complex process and may require further scripting and configuration beyond what is provided here.

- **Disclaimer**: While these tools are free, publishing on platforms like Amazon Kindle Direct Publishing may involve costs depending on file size and distribution.  See Amazon KDP pricing for details.

For more detailed instructions and a complete walkthrough, please watch the YouTube video linked at the top of this description. Good luck with your self-publishing journey!
```

### `book-kindle.css`

```css
/* Keep chapter titles and descriptions together */
.keep-together-toc {
  display: block;
  page-break-inside: avoid;
  break-inside: avoid;
  margin-bottom: 0.75em;
}

.keep-together-toc p:first-child {
  page-break-after: avoid;
  break-after: avoid;
}

.keep-together-toc p:last-child {
  page-break-before: avoid;
  break-before: avoid;
}

body {
  font-size: 1em;
  line-height: 1.4; /* can be 1.4 for instructional titles */
}

.custom-toc h1 {
  margin-top: 0.3em;
}

.pdf-pagebreak,
.pdf-pagebreak-5,
.pdf-linebreak {
  display: none;
}

```

### `book-paperback.css`

```css
.custom-toc h1 {
  margin-top: 1em;
}

.keep-together-toc {
  margin-bottom: 0.75em;
}

.keep-together-toc p em {
  display: block;
}

.keep-together-toc p:first-child {
  margin-bottom: 0.3em;
}

.keep-together-toc p:last-child {
  margin-top: 0;
  margin-bottom: 0.5em;
}

.custom-toc p {
  font-weight: bold;
}

.custom-toc em {
  font-weight: normal;
}

body {
  font-size: 1.15em;
  line-height: 1.4;
}

.pdf-pagebreak {
  page-break-after: always;
}

.pdf-pagebreak-5 {
  page-break-before: always;
  display: block;
  height: 5em;
}

.pdf-linebreak {
  display: block;
  height: 0;
  content: "";
  margin: 0;
  padding: 0;
  line-height: 1.3; /* Match your body line-height */
}

nav {
  display: none;
}

body {
  font-family: "Bitter", serif !important; /* Explicitly specify Bitter */
  font-weight: 400 !important; /* Explicitly set the font weight to regular */
  -webkit-font-smoothing: antialiased !important; /* Try to force consistent anti-aliasing */
  -moz-osx-font-smoothing: grayscale !important; /* Try to force consistent anti-aliasing */
}

p {
  font-family: "Bitter", serif !important; /* Reinforce the font family */
  font-weight: 400 !important; /* Reinforce the font weight */
}

section.level2.section-title {
  height: 1.4em;
}

```

### `book.css`

```css
/* ==================================================
   1. GENERAL TYPOGRAPHY & BASELINE STYLES
   ================================================== */
body {
    font-family: serif;
    widows: 2; /* does not inherit */
    orphans: 2; /* does not inherit */
    text-align: justify;
}

div {
    margin: 0;
    padding: 0;
    widows: 2;
    orphans: 2;
}

p {
  text-indent: 0;
  margin: 0;
}

ul, ol, li, table, p {
  font-family: serif;
}

/* Indented paragraphs except first */
p + p {
  text-indent: 1.5em;
  margin-top: 0.2em;
}

.pagebreak {
  page-break-after: always;
}

hr {
  border: none;
  border-top: 0.75pt solid #000;
  page-break-after: avoid;
  break-after: avoid;
}

img {
  object-fit: contain;
}

/* ==================================================
    2. CHAPTER & HEADING STYLES
  ================================================== */

p.subtitle {
  font-size: 1.3em;
  font-family: sans-serif;
  margin-bottom: 1.5em;
  font-style: italic;
}

/* Chapter Title (Level 1) */
h1 {
  font-weight: normal;
  text-align: right;
  font-family: sans-serif;
  font-size: 2.6em;
  line-height: 1.2em;
  margin-top: 1em;
  margin-bottom: 0;
}

h1.title {
  font-size: 1.8em;
  margin-top: 1em;
  text-align: left;
  /*font-family: sans;*/
}

.chapter-subtitle {
  text-align: right;
  font-family: sans-serif;
  font-style: italic;
  margin-top: 0.6em;
  margin-bottom: 2em;
  line-height: 1.3em;
  font-size: 1.5em;
}

.book-title {
  font-weight: normal;
  text-align: right;
  font-family: sans-serif;
  font-size: 2.6em;
  line-height: 1.2em;
  margin-top: 1.5em;
}

.book-title-main {
  font-weight: normal;
}

.book-title-subtitle {
  font-style: italic;
  margin-top: 0.5em;
  margin-bottom: 2em;
  line-height: 1.3em;
  font-size: 0.7em;
}

.chapter-spacing {
  margin-bottom: 3em;
}

/* Section Title (Level 2) */
.section-title {
  text-align: center;
  font-family: sans-serif;
  font-weight: bold;
  font-size: 1.3em;
  text-transform: uppercase;
  margin-top: 2em;
  margin-bottom: 1em;
  page-break-after: avoid;
  break-after: avoid;
}

.section-title h2 {
  font-size: 1em;
  margin: 0;
}

/* Add rules for direct h2 elements too */
h2 {
  page-break-after: avoid;
  break-after: avoid;
}

/* Make sure the paragraph after a heading stays with it */
h2 + p {
  page-break-before: avoid;
  break-before: avoid;
}

/* Subsection Title (Level 3) */
.subsection-title {
  text-align: left;
  font-family: sans-serif;
  font-weight: bold;
  font-size: 1.1em;
  text-transform: uppercase;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
  page-break-after: avoid;
  break-after: avoid;
}

.subsection-title h3 {
  font-size: 1em;
  margin: 0;
}

/* Add rules for direct h3 elements too */
h3, h4 {
  page-break-after: avoid;
  break-after: avoid;
}

/* Make sure the paragraph after a heading stays with it */
h3 + p, h4 + p {
  page-break-before: avoid;
  break-before: avoid;
}

h4 {
  text-align: left;
  font-family: serif;
  font-weight: bold;
  font-size: 1em;
  margin-top: 1.3em;
  margin-bottom: 0em;
  page-break-after: avoid;
  break-after: avoid;
  line-height: 1.5em;
}

/* ==================================================
    3. LISTS
  ================================================== */
ul, ol {
  margin: 0.5em 0;
  padding-left: 1.5em;
}

li, li {
  margin: 0.5em 0;
/*  page-break-inside: avoid;*/ /* Try to avoid breaking inside list items when possible */
}

/* Keep first paragraph (with strong element) together with subsequent paragraphs */
/*li > p:first-child {
  page-break-after: avoid;
  break-after: avoid;
}*/

/* Keep subsequent paragraphs with the first paragraph */
li > p:first-child + p {
  page-break-before: avoid;
  break-before: avoid;
}

li strong {
  font-weight: bold;
}

ol p + p, ul p + p {
  text-indent: initial;
  margin-top: 0.5em;
}

ol.toc {
  list-style: none;
}

/* ==================================================
    4. TABLES
  ================================================== */
table {
  width: 95%;
  border-collapse: collapse;
  margin: 1em;
  font-size: 0.9em;
}

table, th, td {
  border: 1px solid black;
}

th, td {
  padding: 0.4em;
  text-align: left;
}

/* ==================================================
    5. IMAGES & FIGURES
  ================================================== */
/* Center figures and images */
figure {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin: auto;
  margin-top: 0.35em;
  margin-bottom: 0.35em;
  page-break-inside: avoid;
}

figure img {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 0 auto;
}

figcaption {
  text-align: center;
  font-style: italic;
  margin-top: 0.3em;
  margin-bottom: 0;
  page-break-after: avoid;
  display: none;
}

/* Full-page image centering */
.full-page-image {
  height: 100vh; /* Full viewport height */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0;
  padding: 0;
  page-break-before: always;
}

.full-page-image figure {
  margin: 0;
}

/* For print, use alternative approach for vertical centering */
@media print {
  .full-page-image {
    height: auto;
    position: relative;
    top: 50%;
    transform: translateY(-50%);
  }
}

img[width] {
  max-width: 100%;
  height: auto;
}

p:has(img) {
  text-align: center;
}

p img {
  display: block;
  margin: 0 auto;
  max-width: 100%;
  height: auto;
}

/* Image container for centered images */
.image-container {
  text-align: center;
  margin: 1em 0;
}

.image-container img {
  display: inline-block;
  max-width: 100%;
}

/* ==================================================
    6. CUSTOM TOC STYLING
  ================================================== */
.custom-toc, .custom-toc h1 {
  text-align: center;
}

.custom-toc .chapter-spacing {
  margin-bottom: 2em;
}

.custom-toc p + p {
  text-indent: initial;
}

.custom-toc p {
  margin-left: 1.5em;
  margin-right: 1.5em;
}

.custom-toc em {
  font-size: 0.9em;
  opacity: 0.8;
}

.custom-toc hr {
  margin: 1.25em 7em;
}

.custom-toc .chapter-subtitle {
  margin: 0;
  height: 0;
}

.empty-line-35 {
  height: 0.35em;
  line-height: 0;
  content: "";
  display: block;
}

.empty-line-70 {
  height: 0.7em;
  line-height: 0;
  content: "";
  display: block;
}

.empty-line-100 {
  height: 1em;
  line-height: 0;
  content: "";
  display: block;
}

/* Keep chapter titles and descriptions together */
.keep-together {
  display: block;
  page-break-inside: avoid;
  break-inside: avoid;
}

.keep-together p:first-child {
  page-break-after: avoid;
  break-after: avoid;
}

.keep-together p:last-child {
  page-break-before: avoid;
  break-before: avoid;
  margin-bottom: 0.7em;
}

/* ==================================================
    Manifesto-specific styles
  ================================================== */
.manifesto {
  text-align: center;
}

.manifesto p {
  margin-left: 1em;
  margin-right: 1em;
}

.manifesto h1 {
  /*margin-top: 0.3em;*/
  text-align: center;
}

.manifesto .chapter-spacing {
  margin-bottom: 4em;
}

.manifesto p + p {
  text-indent: initial;
}

.manifesto em {
  font-size: inherit;
  opacity: 0.8;
}

.manifesto hr {
  margin: 2em 7em;
}

.manifesto .chapter-label {
  font-size: 2.5em;
  font-weight: bold;
}

.manifesto .chapter-subtitle {
  margin: 0;
  height: 0;
}

.manifesto .keep-together em {
  font-size: 0.75em;
  opacity: 1;
}

.manifesto .keep-together p {
  font-size: 1.3em;
  line-height: 1.1em;
}

/* ==================================================
    7. CALLOUTS & BLOCKQUOTES
  ================================================== */
blockquote {
  font-style: italic;
  margin-left: 1.5em;  
  margin-right: 1.5em;
  padding: 0.5em;
}

/* Base callout styles */
.callout {
  margin: 1.3em 0;
  padding: 0 1em;
  border-left: 0.25em solid;
}

.callout p {
  margin-top: 0.5em;
}

.callout p + p {
  text-indent: initial;
}

.callout-content {
  margin-top: 0.5em;
  line-height: 1.5em;
}

.callout-content p {
  margin: 0.5em 0;
}

/* Callout header formatting */
.callout-header {
  display: flex;
  align-items: center;
  page-break-after: avoid;
  break-after: avoid;
}

.callout-header > *:not(:last-child) {
  margin-right: 8px;
}

.callout-header p {
  display: inline-flex;
  align-items: center;
  margin: 0;
  margin-right: 0.5em;
}

.callout-header p > *:not(:last-child) {
  margin-right: 8px;
}

/* Keep first paragraph with callout header */
.callout-header + p {
  page-break-before: avoid;
  break-before: avoid;
}

.callout-header strong {
  font-weight: bold;
  white-space: nowrap;
}

.callout-header img {
  display: inline-block;
  vertical-align: middle;
}

.callout-title {
  font-weight: bold;
  margin-bottom: 0.75em;
  display: flex;
  align-items: center;
}

.callout-title > *:not(:last-child) {
  margin-right: 0.5em;
}

/* Action callout */
[data-callout="action"] {
  border-left-color: #FF6B6B;
}

[data-callout="action"] .callout-title::before {
  content: "►";
}

/* Story callout */
[data-callout="story"] {
  border-left: none;
  font-style: italic;
  padding: 0 2.5em;
}

/* Style for the story icon paragraph */
img.icon-story {
  width: 50%;
  height: auto;
  display: block;
  margin: 0 auto;
}

/* Style for story title paragraph */
p.story-title {
  text-align: center;
  font-style: italic;
  font-weight: bold;
  font-size: 1.2em;
  margin-top: 1em;
  margin-bottom: 0.5em;
}

/* Keep icon with first two paragraphs - new rules */
[data-callout="story"] > p:first-child {
  page-break-after: avoid;
  break-after: avoid;
}

[data-callout="story"] > p:first-child + p {
  page-break-before: avoid;
  break-before: avoid;
  page-break-after: avoid;
  break-after: avoid;
}

[data-callout="story"] > p:first-child + p + p {
  page-break-before: avoid;
  break-before: avoid;
}

/* Summary callout */
[data-callout="summary"] {
  border-left-color: #69DB7C;
}

[data-callout="summary"] .callout-title::before {
  content: "※";
}

/* ==================================================
    8. MEDIA QUERIES - DARK MODE & E-INK
  ================================================== */
/* Dark mode adjustments */
@media (prefers-color-scheme: dark) {
  [data-callout="story"] .callout-title {
    color: #7FC3F7;
  }
  
  [data-callout="action"] {
    border-left-color: #FF9999;
  }
  
  [data-callout="story"] {
    border-left-color: #7FC3F7;
  }
  
  [data-callout="summary"] {
    border-left-color: #90E6A0;
  }
}

/* E-ink specific adjustments */
@media (monochrome) {
  .callout {
    border-left-width: 0.35em;
    background-color: transparent !important;
    color: #000 !important;
  }
  
  [data-callout] {
    background-color: transparent !important;
  }
  
  [data-callout="action"] {
    border-left-color: #000;
  }
  
  [data-callout="story"] {
    border-left-color: #444;
  }
  
  [data-callout="summary"] {
    border-left-color: #888;
  }
}

/* ==================================================
   9. PAGE BREAK CONTROLS & FIRST-ON-PAGE STYLING
   ================================================== */

/* Target elements that appear after page breaks */
div[style*="page-break-after"] + .section-title,
div[style*="page-break-after"] + section > h2,
div[style*="page-break-after"] + h2 {
  margin-top: 0;     /* Remove top margin when appearing after page break */
}

/* Keep original selectors as fallback */
.section-title:first-child,
h2:first-child {
  margin-top: 0;     /* Remove top margin when first on page */
}

/* Target elements that appear after page breaks */
div[style*="page-break-after"] + .subsection-title,
div[style*="page-break-after"] + section > h3,
div[style*="page-break-after"] + h3 {
  margin-top: 0;     /* Remove top margin when appearing after page break */
}

/* Keep original selectors as fallback */
.subsection-title:first-child,
h3:first-child {
  margin-top: 0;     /* Remove top margin when first on page */
}


/* ===================================================
   10. REFERENCES
   ================================================== */

.references {
  text-align: left;
}

/* Remove bullets and all indentation from reference lists */
.references ul {
  list-style-type: none;
  padding-left: 0;
  margin-left: 0;
}

/* Remove all indentation from list items */
.references li {
  text-indent: 0;
  padding-left: 0;
  margin-bottom: 0.7em;
}

/* Ensure paragraphs in references have no text indent */
.references li p {
  text-indent: 0;
}

/* Override any potential indentation for adjacent paragraphs */
.references li p + p {
  text-indent: 0;
  margin-left: 0;
}

/* Override the general p + p rule that adds indentation to paragraphs */
.references p + p {
  text-indent: 0;
}

```

### `export.lua`

```lua
-- This script processes callouts in a Pandoc document and
-- modifies the header levels for chapters, sections, and subsections.
-- It also adds specific classes to the headers and callouts based on their types.

local stringify = (require "pandoc.utils").stringify



-- --------------------------------
-- Processinging Obisidian Callouts
-- --------------------------------

-- An Obsidian callout is a blockquote that starts with `[!Type]`.
-- Callouts offer a way to structure information in a document and format them visually.
-- > [!Type] Title
-- > 
-- > Content
-- > continued...

-- Mapping of callout types to icon filenames
local callout_icons = {
  example = "../images/ico-example.png",
  story = "../images/ico-story.png",
  definition = "../images/ico-definition.png",
  practice = "../images/ico-practice.png",
  takeaway = "../images/ico-takeaway.png",
  mastery = "../images/ico-mastery.png",
  abstract = "../images/ico-abstract.png"
}

-- Function to process the document and transform callouts
function Pandoc(doc)
  local function is_callout(el)
    if el.t ~= "BlockQuote" then return false end
    local first = el.content[1]
    if not (first and first.t == "Para") then return false end
    local first_element = first.content[1]

    -- Ensure first element exists and is a string (Str)
    if not (first_element and first_element.t == "Str") then return false end

    -- Check if it starts with [!Type]
    return first_element.text:match("^%[!(%w+)%]") ~= nil
  end

  local function transform(blocks)
    local new_blocks = {}

    for _, block in ipairs(blocks) do
      if is_callout(block) then
        -- Extract callout type and title
        local first_para = block.content[1]
        if not first_para or first_para.t ~= "Para" or #first_para.content == 0 then
          table.insert(new_blocks, block)
          goto continue
        end

        -- Extract `[!Type]` and capture the remaining text as the title
        local first_element = first_para.content[1]
        local ctype = first_element.text:match("^%[!(%w+)%]")
        if ctype then
          ctype = ctype:lower()
        else
          ctype = "note"
        end

        -- Remove `[!Type]` from the first element
        first_element.text = first_element.text:gsub("^%[!(%w+)%]%s*", "")

        -- Collect full title across multiple elements
        local title_parts = {}
        local index = 1

        -- Start collecting title parts after `[!Type]`
        while first_para.content[index] do
          local inline = first_para.content[index]
          
          -- First check if this is the start of content (not title)
          if index > 1 and first_para.content[index-1].t == "SoftBreak" then
            break -- Stop at line breaks - this indicates we're into the content
          end
          
          -- Include ALL types of elements in the title
          table.insert(title_parts, inline)
          index = index + 1
        end

        -- Remove title from paragraph
        for _ = 1, index - 1 do
          table.remove(first_para.content, 1)
        end

        -- Create callout div
        local div = pandoc.Div(block.content, {class = "callout"})
        div.attributes["data-callout"] = ctype
        
        -- Create callout header content
        local callout_header_content = {}
        local icon_file = callout_icons[ctype]
		
		-- Special handling for story callouts
		if ctype == "story" then
		  if icon_file then
		    local attr = pandoc.Attr("", {"icon-story"}) 
            local icon_image = pandoc.Image("", icon_file, "", attr)
            icon_image.attributes["alt"] = ""
            table.insert(callout_header_content, icon_image)
          end
          
          -- Create the header with just the image
          local callout_header = pandoc.Para(callout_header_content)
          
          -- Insert the header at the top of the callout
          table.insert(div.content, 1, callout_header)
          
          -- Add title in a separate paragraph after the image if it exists
          if #title_parts > 0 then
            local title_text = pandoc.utils.stringify(title_parts):gsub("^%s+", ""):gsub("%s+$", "")
            local html = string.format('<p class="story-title">%s</p>', title_text)
            table.insert(div.content, 2, pandoc.RawBlock("html", html))
          end
          
          -- Add the story callout to new_blocks
          table.insert(new_blocks, div)
		
		else
			if icon_file then
			  local icon_image = pandoc.Image("", icon_file)
			  icon_image.attributes["width"] = "24"
			  icon_image.attributes["height"] = "24"
			  icon_image.attributes["alt"] = ""

			  table.insert(callout_header_content, icon_image)
			end

			-- Add extracted title in bold - pass all title elements
			if #title_parts > 0 then
			  table.insert(callout_header_content, pandoc.Strong(title_parts))
			end

			-- Ensure inline elements stay in the same line
			local callout_header = pandoc.Div({pandoc.Para(callout_header_content)}, {class = "callout-header"})

			-- Insert header at the top of the callout
			table.insert(div.content, 1, callout_header)

			table.insert(new_blocks, div)
		end
      else
        -- Keep all normal blockquotes unchanged
        table.insert(new_blocks, block)
      end
      ::continue::
    end

    return new_blocks
  end

  doc.blocks = transform(doc.blocks)
  return doc
end



-- ------------------------------
-- Processing Headers
-- ------------------------------

function Header(el)
  -- CHAPTER TITLE: Level 1
  if el.level == 1 then
    local title_text = pandoc.utils.stringify(el.content)
    local main_title, subtitle = title_text:match("^(.-):%s*(.*)$")
    if not main_title then
      main_title = title_text
      subtitle = ""
    end
	
	if main_title == "Sketch Your Mind" then
      subtitle = "Nurture a Playful and Creative Brain"
    end

    -- Construct two-line chapter title with spacing
    if subtitle == "" then
      local result = {
        pandoc.Header(1, pandoc.Str(main_title)),
          pandoc.RawBlock("html", '<div class="chapter-spacing"></div>')
        }
        return result    
    else
      local result = {
        pandoc.Header(1, pandoc.Str(main_title)),
          pandoc.RawBlock("html", '<div class="chapter-subtitle"><em>' .. subtitle .. '</em></div>'),
          pandoc.RawBlock("html", '<div class="chapter-spacing"></div>')
        }
        return result    
    end
  -- SECTION: Level 2
  elseif el.level == 2 then
    -- Text already converted to uppercase in PowerShell script
    return pandoc.Div({pandoc.Header(2, el.content)}, {class = "section-title"})

  -- SUBSECTION: Level 3
  elseif el.level == 3 then
    -- Text already converted to uppercase in PowerShell script
    return pandoc.Div({pandoc.Header(3, {pandoc.Strong(el.content)})}, {class = "subsection-title"})
  end

  return el
end

```

### `metadata-kindle.yaml`

```yaml
---
title: "Sketch Your Mind"
subtitle: "Nurture a Playful and Creative Brain"
author: "Written by Zsolt Viczián"
date: "First published by Zsolt Viczián in 2025"
language: "en-US"
cover-image: "../images/sym-cover.png"
rights: "© 2025 Zsolt Viczián. All rights reserved."
description: "Sketch Your Mind: Nurture a Playful and Creative Brain shows how to break free from text-first thinking and embrace a visual approach to personal knowledge management. It explains how 4D PKM integrates sketches, diagrams, and spatial layouts to reveal hidden connections and spark deeper insights. Drawing on stories, examples, and practical tools, it encourages readers to build playful “Idea Integration Boards” and “Visual Zettelkasten” networks. Each chapter highlights small steps to transform scattered notes into a living ecosystem of ideas that evolve over time. By reactivating our innate ability to think visually, the book offers a path to clarity, creativity, and truly meaningful learning."
identifier:
  - scheme: ISBN-13
    text: 978-615-02-3323-9
lang: "en"
encoding: "utf-8"
---
```

### `metadata-paperback.yaml`

```yaml
---
title: "Sketch Your Mind"
subtitle: "Nurture a Playful and Creative Brain"
author: "Written by Zsolt Viczián"
date: "First published by Zsolt Viczián in 2025"
language: "en-US"
cover-image: "../images/sym-cover.png"
rights: "© 2025 Zsolt Viczián. All rights reserved."
description: "Sketch Your Mind: Nurture a Playful and Creative Brain shows how to break free from text-first thinking and embrace a visual approach to personal knowledge management. It explains how 4D PKM integrates sketches, diagrams, and spatial layouts to reveal hidden connections and spark deeper insights. Drawing on stories, examples, and practical tools, it encourages readers to build playful “Idea Integration Boards” and “Visual Zettelkasten” networks. Each chapter highlights small steps to transform scattered notes into a living ecosystem of ideas that evolve over time. By reactivating our innate ability to think visually, the book offers a path to clarity, creativity, and truly meaningful learning."
identifier:
  - scheme: ISBN-13
    text: 978-615-02-3320-8
lang: "en"
encoding: "utf-8"
---
```
