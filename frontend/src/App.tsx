import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Loader2, Github, CheckCircle2, XCircle } from 'lucide-react';

export const Home = () => {
  const [githubLink, setGithubLink] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [status, setStatus] = useState<{
    type: 'success' | 'error' | null;
    message: string;
  }>({ type: null, message: '' });

  const handleSubmit = async (e: React.MouseEvent | React.KeyboardEvent) => {
    e.preventDefault();

    const githubRegex = /^https?:\/\/(www\.)?github\.com\/.+/;
    if (!githubRegex.test(githubLink)) {
      setStatus({
        type: 'error',
        message: 'Please enter a valid GitHub URL'
      });
      return;
    }

    setIsLoading(true);
    setStatus({ type: null, message: '' });

    try {
      const response = await fetch('/api/upload', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ githubLink }),
      });

      if (!response.ok) {
        throw new Error('Failed to process GitHub link');
      }

      const data = await response.json();
      console.log(data);

      setStatus({
        type: 'success',
        message: 'GitHub link processed successfully!'
      });
      setGithubLink('');
    } catch (error) {
      setStatus({
        type: 'error',
        message: error instanceof Error ? error.message : 'An error occurred'
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4 bg-linear-to-br from-background to-muted">
      <Card className="w-full max-w-md">
        <CardHeader className="space-y-1">
          <div className="flex items-center justify-center mb-4">
            <div className="p-3 rounded-full bg-primary/10">
              <Github className="w-8 h-8 text-primary" />
            </div>
          </div>
          <CardTitle className="text-2xl text-center">GitHub Repository</CardTitle>
          <CardDescription className="text-center">
            Enter a GitHub repository URL to analyze
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="space-y-2">
              <Input
                type="url"
                placeholder="https://github.com/username/repository"
                value={githubLink}
                onChange={(e) => setGithubLink(e.target.value)}
                disabled={isLoading}
                className="w-full"
                onKeyDown={(e) => {
                  if (e.key === 'Enter') {
                    handleSubmit(e);
                  }
                }}
              />
            </div>

            {status.type && (
              <Alert variant={status.type === 'error' ? 'destructive' : 'default'}>
                <div className="flex items-start gap-2">
                  {status.type === 'success' ? (
                    <CheckCircle2 className="h-4 w-4 mt-0.5" />
                  ) : (
                    <XCircle className="h-4 w-4 mt-0.5" />
                  )}
                  <AlertDescription>{status.message}</AlertDescription>
                </div>
              </Alert>
            )}

            <Button
              onClick={handleSubmit}
              className="w-full"
              disabled={isLoading || !githubLink}
            >
              {isLoading ? (
                <>
                  <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                  Processing...
                </>
              ) : (
                'Submit'
              )}
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};