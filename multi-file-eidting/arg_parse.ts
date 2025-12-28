export function getTranscriptFilePath(): string {
  return process.argv[2] || "./transcript.txt";
}
