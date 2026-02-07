import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Loader2, Link2, FileText } from "lucide-react"

export const App = () => {
  const [link, setLink] = useState("")
  const [result, setResult] = useState("")
  const [loading, setLoading] = useState(false)

  const handleSubmit = async () => {
    if (!link.trim()) return

    setLoading(true)
    // Simulate processing - replace with actual API call
    setTimeout(() => {
      setResult(`Processed: ${link}`)
      setLoading(false)
    }, 2000)
  }

  return (
    <div className="min-h-screen bg-linear-to-br from-background via-background to-muted/30 flex items-center justify-center p-4">
      <div className="w-full max-w-lg space-y-8">
        

        <div className="text-center space-y-2">
          <h1 className="text-3xl font-semibold tracking-tight">
            Repo Doc Agent
          </h1>
          <p className="text-muted-foreground text-sm">
            Enter a GitHub repository link to generate documentation
          </p>
        </div>

        <div className="relative group">
          <div className="absolute -inset-0.5 bg-linear-to-r from-primary/20 to-primary/5 rounded-lg blur opacity-50 group-hover:opacity-100 transition duration-500" />
          <div className="relative flex items-center gap-2 bg-card border border-border/50 rounded-lg p-2">
            <Link2 className="w-5 h-5 text-muted-foreground ml-2" />
            <Input
              type="url"
              placeholder="https://github.com/username/repository"
              value={link}
              onChange={(e) => setLink(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
              className="border-0 bg-transparent focus-visible:ring-0 focus-visible:ring-offset-0 shadow-none"
            />
            <Button
              onClick={handleSubmit}
              disabled={loading || !link.trim()}
              size="sm"
              className="mr-1"
            >
              {loading ? (
                <Loader2 className="w-4 h-4 animate-spin" />
              ) : (
                "Generate"
              )}
            </Button>
          </div>
        </div>

        {/* Result Box */}
        {result && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div className="bg-card/80 backdrop-blur-sm border border-border/50 rounded-lg p-4">
              <div className="flex items-start gap-3">
                <FileText className="w-5 h-5 text-primary mt-0.5" />
                <div className="space-y-1">
                  <p className="text-sm font-medium">Result</p>
                  <p className="text-sm text-muted-foreground">{result}</p>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

