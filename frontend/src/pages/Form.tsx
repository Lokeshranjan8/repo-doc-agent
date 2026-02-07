import { useEffect, useState } from "react";

export default function Form() {
  const originalText = "Paste a link above and the processed output will appear here.";

  const [link, setLink] = useState("");
  const [output, setOutput] = useState(originalText);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (link.trim() === "") {
      setOutput(originalText);
      setLoading(false);
      return;
    }

    setLoading(true);
    const timer = setTimeout(() => {
      setOutput(`Processed output for: ${link}`);
      setLoading(false);
    }, 2000);

    return () => clearTimeout(timer);
  }, [link]);

  return (
    <div className="min-h-screen flex items-center justify-center bg-background font-sans text-foreground p-6">
      <div className="w-full max-w-[520px] bg-card p-10 rounded-lg shadow-xl border border-border flex flex-col gap-8 transition-all duration-300">
        
        {/* Header Section */}
        <div className="space-y-2">
          <h1 className="text-3xl font-serif font-bold text-primary tracking-tight">
            Paste the link you want to Explore
          </h1>
          <p className="text-muted-foreground text-sm">
            Enter your URL below to generate things.
          </p>
        </div>

        {/* Input Group */}
        <div className="flex flex-col gap-2">
          <label className="text-xs uppercase tracking-widest font-semibold text-muted-foreground ml-1">
            Source URL
          </label>
          <input
            type="text"
            placeholder="https://example.com"
            value={link}
            onChange={(e) => setLink(e.target.value)}
            className="px-4 py-4 bg-input/10 text-foreground border border-input rounded-md focus:outline-none focus:ring-2 focus:ring-primary/40 transition-all font-mono text-sm"
          />
        </div>

        {/* Status & Output */}
        <div className="flex flex-col gap-2">
          <div className="flex justify-between items-center px-1">
             <label className="text-xs uppercase tracking-widest font-semibold text-muted-foreground">
              Output
            </label>
            {loading && (
              <span className="text-xs animate-pulse text-primary font-medium">
                Processing...
              </span>
            )}
          </div>
          
          <div className={`h-48 border rounded-md p-5 text-sm leading-relaxed overflow-auto transition-colors
            ${loading ? 'bg-muted/30 border-primary/20' : 'bg-secondary/20 border-border'}
          `}>
            <p className={output === originalText ? "italic text-muted-foreground" : "text-foreground font-serif"}>
              {loading ? "" : output}
            </p>
          </div>
        </div>

        {/* Action Button */}
        <button
          className="bg-primary text-primary-foreground py-4 rounded-md font-bold text-sm uppercase tracking-widest hover:opacity-90 active:scale-[0.98] transition-all shadow-md"
        >
          Process Now
        </button>
      </div>
    </div>
  );
}